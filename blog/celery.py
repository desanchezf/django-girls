
import os 

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

app = Celery('blog', broker=os.environ.get('BROKER_URL'))
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()