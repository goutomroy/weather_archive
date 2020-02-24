from enum import IntEnum
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from weather import tasks


class StatusTypes(IntEnum):
    PENDING = 1
    RUNNING = 2
    COMPLETE = 3
    FAILURE = 4

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Archive(models.Model):
    file = models.FileField(upload_to='archive/%Y/%m/%d/',
                                    validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    status = models.PositiveSmallIntegerField(default=StatusTypes.PENDING, choices=StatusTypes.choices())
    created = models.DateField(help_text=_("Archive creation date.",), auto_now_add=True, editable=False)

    def __str__(self):
        return self.file.name


@receiver(post_save, sender=Archive)
def process_archive(sender, *args, **kwargs):
    if kwargs.get('created', False):
        archive = kwargs.get('instance')
        tasks.process_archive.apply_async([archive.id])

