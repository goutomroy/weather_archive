import csv
import datetime
import logging
from django.db import transaction, DatabaseError

from weather.celery import app

logger = logging.getLogger(__name__)


@app.task(bind=True)
def process_archive(self, archive_id):
    from apps.archive.models import Archive, Observation
    from apps.archive.models import StatusTypes

    try:
        archive = Archive.objects.get(id=int(archive_id))
        archive.status = StatusTypes.RUNNING
        archive.save()
        observations = []
        logger.info(f'file_path : {archive.file.path}')
        with open(archive.file.path, newline='') as f:
            reader = csv.reader(f)
            for index, row in enumerate(list(reader)):
                if index == 0:
                    continue
                d = Observation()
                dt = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
                d.date = dt.astimezone(tz=None)
                d.temperature = float(row[1])
                d.rainfall = float(row[2])
                d.barometricPressure = float(row[3])
                d.humidity = int(row[4])
                d.windSpeed = int(row[5])
                d.windDirection = row[6]
                observations.append(d)
        try:
            with transaction.atomic():
                Observation.objects.bulk_create(observations)
                archive.status = StatusTypes.COMPLETE
                archive.save()
        except DatabaseError:
            raise Exception

    except Exception as exc:
        logger.error(exc)
        archive.status = StatusTypes.FAILURE
        archive.save()

