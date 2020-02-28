import csv
import datetime
import logging
from django.db import transaction
from weather.celery import app
from apps.archive.models import Archive, Observation
from apps.archive.models import StatusTypes

logger = logging.getLogger(__name__)


@app.task(bind=True)
def process_archive(self, archive_id):
    try:
        archive = Archive.objects.get(id=int(archive_id))
        archive.status = StatusTypes.RUNNING
        archive.save()
        observations = []
        with open(archive.file.path, newline='') as f:
            reader = csv.reader(f)
            for index, row in enumerate(list(reader)):
                if index == 0:
                    continue
                d = Observation(date=datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S').astimezone(tz=None),
                                temperature=float(row[1]), rainfall=float(row[2]), barometricPressure=float(row[3]),
                                humidity=int(row[4]), windSpeed=int(row[5]), windDirection=row[6])
                observations.append(d)

        with transaction.atomic():
            Observation.objects.bulk_create(observations)
            archive.status = StatusTypes.COMPLETE
            archive.save()

    except Exception as exc:
        logger.error(exc)
        archive.status = StatusTypes.FAILURE
        archive.save()
