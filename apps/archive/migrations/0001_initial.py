# Generated by Django 3.0.3 on 2020-03-01 22:32

import apps.archive.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='archive/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])])),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'PENDING'), (2, 'RUNNING'), (3, 'COMPLETE'), (4, 'FAILURE')], default=apps.archive.models.StatusTypes['PENDING'])),
                ('created', models.DateField(auto_now_add=True, help_text='Archive creation date.')),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Observation date.')),
                ('temperature', models.FloatField()),
                ('rainfall', models.FloatField()),
                ('barometricPressure', models.FloatField()),
                ('humidity', models.IntegerField()),
                ('windSpeed', models.IntegerField()),
                ('windDirection', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('done', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
