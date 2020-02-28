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

        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            for index, row in enumerate(list(reader)):
                if index == 0:
                    continue
                d = {'date': datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S').astimezone(tz=None),
                     'temperature': float(row[1]), 'rainfall': float(row[2]), 'barometricPressure': float(row[3]),
                     'humidity': int(row[4]), 'windSpeed': int(row[5]), 'windDirection': row[6]}
                columns.append(d)

        logger.info(columns)
        logger.info(f'file_path : {file_path}')
        logger.info(f'number of rows : {len(columns)}')



