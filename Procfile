release: python src/manage.py migrate
worker: celery worker -A src/celery_app -l INFO
web: gunicorn src.RemindMe.wsgi --log-file -
