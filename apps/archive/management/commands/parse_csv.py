import datetime
import logging
import os
import csv
from django.conf import settings
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'data/weather_archive.csv')

        columns = []
        # with open(file_path, newline='') as f:
        #     reader = csv.DictReader(f)
        #     for row in reader:
        #         row_as_dict = {k: v for k, v in row.items()}
        #         columns.append(row_as_dict)

        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            for index, row in enumerate(list(reader)):
                if index == 0:
                    continue
                d = {}
                dt = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
                d['date'] = dt.astimezone(tz=None)
                d['temperature'] = float(row[1])
                d['rainfall'] = float(row[2])
                d['barometricPressure'] = float(row[3])
                d['humidity'] = int(row[4])
                d['windSpeed'] = int(row[5])
                d['windDirection'] = row[6]
                columns.append(d)

        logger.info(columns)
        logger.info(f'file_path : {file_path}')
        logger.info(f'number of rows : {len(columns)}')



