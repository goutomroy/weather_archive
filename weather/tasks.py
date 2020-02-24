import logging
from weather.celery import app

logger = logging.getLogger(__name__)


@app.task(bind=True)
def process_archive(self, archive_id):
    from apps.archive.models import Archive
    from apps.archive.models import StatusTypes

    try:
        archive = Archive.objects.get(id=int(archive_id))
        archive.status = StatusTypes.RUNNING
        archive.save()

        logger.info(f"---------{archive.file.path}")

        archive.status = StatusTypes.COMPLETE
        archive.save()
    except Exception as exc:
        archive.status = StatusTypes.FAILURE
        archive.save()

