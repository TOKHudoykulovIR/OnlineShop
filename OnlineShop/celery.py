import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineShop.settings')

app = Celery('OnlineShop')
app.config_from_object('django.conf:settings', namespace='CELERY')  # load any custom configuration from your project settings using the config_from_object()
app.autodiscover_tasks()  # tell Celery to auto-discover asynchronous tasks for your applications. Celery will look for a tasks.py file in each application
