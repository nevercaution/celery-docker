import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'common.settings')

from django.conf import settings

app = Celery('common')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, related_name="celery_task")


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
