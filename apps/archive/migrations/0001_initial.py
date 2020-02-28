# Generated by Django 3.0.3 on 2020-02-24 20:55

import apps.archive.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archive_file', models.FileField(upload_to='archive/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])])),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'PENDING'), (2, 'RUNNING'), (3, 'COMPLETE'), (4, 'FAILURE')], default=apps.archive.models.StatusTypes['PENDING'])),
                ('created', models.DateField(auto_now_add=True, help_text='Archive creation date.')),
            ],
        ),
    ]