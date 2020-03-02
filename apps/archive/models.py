from enum import IntEnum
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token


class StatusTypes(IntEnum):
    PENDING = 1
    RUNNING = 2
    COMPLETE = 3
    FAILURE = 4

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Observation(models.Model):
    date = models.DateField(help_text=_("Observation date.", ))
    temperature = models.FloatField()
    rainfall = models.FloatField()
    barometricPressure = models.FloatField()
    humidity = models.IntegerField()
    windSpeed = models.IntegerField()
    windDirection = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.date}->{self.temperature}"


class Archive(models.Model):
    file = models.FileField(upload_to='archive/%Y/%m/%d/', validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    status = models.PositiveSmallIntegerField(default=StatusTypes.PENDING, choices=StatusTypes.choices())
    created = models.DateField(help_text=_("Archive creation date.",), auto_now_add=True, editable=False)

    def __str__(self):
        return self.file.name


class Task(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_profile(sender, *args, **kwargs):
    if kwargs.get('created', False):
        Token.objects.get_or_create(user=kwargs.get('instance'))


@receiver(post_save, sender=Archive)
def process_archive(sender, *args, **kwargs):
    if kwargs.get('created', False):
        archive = kwargs.get('instance')
        from weather import tasks
        tasks.process_archive.apply_async([archive.id])


