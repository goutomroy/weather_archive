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
            reader = csv.DictReader(f)
            for row in reader:
                row_as_dict = {k: v for k, v in row.items()}
                columns.append(row_as_dict)

        logger.info(columns)
        logger.info(file_path)
        logger.info(len(columns))



