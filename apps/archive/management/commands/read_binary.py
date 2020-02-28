import logging
import os
from django.conf import settings
from bitstring import BitArray, Bits
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    # 2016-03-23 18: 50:00, 32.3, 0.0, 29.979, 78, 2, ESE

    def read_binary(self, file_path):
        single_bytes = []
        from functools import partial
        with open(file_path, 'rb') as file:
            for byte in iter(partial(file.read, 1), b''):
                byte = ord(byte)
                one_zero = bin(byte)[2:].rjust(8, '0')
                single_bytes.append(one_zero)

        rows = [single_bytes[i:i + 13] for i in range(0, len(single_bytes), 13)]

        data_list = []
        for each_row in rows:
            date_bits = each_row[0] + each_row[1]
            year = int(date_bits[:7], 2)
            month = int(date_bits[7:11], 2)
            day = int(date_bits[11:], 2)
            # date_value = (year - 2000) * 512 + month * 32 + day
            # logger.info(f"date_value: {date_value}")
            time_bits = each_row[2] + each_row[3]
            hour = int(time_bits[5:10], 2)
            minute = int(time_bits[10:], 2)

            temperature = Bits(bin=each_row[4] + each_row[5]).intle / 10
            rainfall = Bits(bin=each_row[6] + each_row[7]).intle / 100
            barometric_pressure = Bits(bin=each_row[8] + each_row[9]).intle / 1000
            humidity = Bits(bin=each_row[10]).intle
            wind_speed = Bits(bin=each_row[11]).intle
            wind_direction = Bits(bin=each_row[12]).intle

            data_list.append(f"year: {year} month: {month} day:{day} "
                             f"hour: {hour} minute: {minute}, "
                             f"temp: {temperature}, "
                             f"rainfall: {rainfall}, "
                             f"barometric pressure: {barometric_pressure}, "
                             f"humidity: {humidity}, "
                             f"wind_speed: {wind_speed}, "
                             f"wind_direction: {wind_direction} ")
        logger.info(data_list[0])

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, 'data/weather_archive.bin')
        self.read_binary(file_path)

        columns = []
        # with open(file_path, "rb") as file:
        #     callable = lambda: file.read(1024)
        #     sentinel = bytes()  # or b''
        #     for chunk in iter(callable, sentinel):
        #         for byte in chunk:
        #             print(byte)

        # for byte in pathlib.Path(file_path).read_bytes():
        #     columns.append(byte)

        # d['date'] = dt.astimezone(tz=None)
        # d['temperature'] = float(row[1])
        # d['rainfall'] = float(row[2])
        # d['barometricPressure'] = float(row[3])
        # d['humidity'] = int(row[4])
        # d['windSpeed'] = int(row[5])
        # d['windDirection'] = row[6]

        # from functools import partial
        # with open(file_path, 'rb') as file:
        #     for byte in iter(partial(file.read, 1), b''):
        #         # date_bi = byte[0]
        #         columns.append(byte)
        # columns.append(byte.decode("utf-8", errors="ignore"))
        # row_format = '4peeeBBB'
        # buffer = unpack(row_format, byte)
        # columns.append(buffer)
        # bb = binascii.unhexlify(byte)
        # columns.append(bb)
        # columns.append(byte)
        # output_numbers = list(byte)
        # columns.append(output_numbers)

        # logger.info(columns)
        # logger.info(type(columns[0]))
        # logger.info(f'file_path : {file_path}')
        # logger.info(f'number of rows : {len(columns)}')

        # 2016 - 03 - 24 03: 05:00, 29.6, 0.0, 29.84, 95, 6, NE
        # [120, 32, 197, 0, 40, 1, 0, 0, 144, 116, 95, 6, 2]
