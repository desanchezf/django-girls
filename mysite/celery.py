from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite', broker=os.environ.get('BROKER_URL'))
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
