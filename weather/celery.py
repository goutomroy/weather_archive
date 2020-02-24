from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
from celery.schedules import crontab
from kombu import Exchange, Queue

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')


class Config:
    imports = ('weather.tasks', )
    broker_url = 'redis://redis/2'
    result_backend = 'django-db'
    beat_max_loop_interval = 600
    result_cache_max = 1000
    # worker_concurrency = 4
    task_compression = 'gzip'
    result_compression = 'gzip'
    task_default_queue = 'low'
    task_serializer = 'json'
    result_serializer = 'json'
    accept_content = ['json']
    timezone = 'UTC'
    enable_utc = True
    result_persistent = True
    task_track_started = True
    task_publish_retry = True


app = Celery('weather')
app.config_from_object(Config)
# app.autodiscover_tasks()