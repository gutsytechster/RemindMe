from celery import Celery
from django.conf import settings

from src.base.services import _set_django_settings_module

_set_django_settings_module()

app = Celery("tasks")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
