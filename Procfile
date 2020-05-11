release: python src/manage.py migrate
worker: python src/manage.py process_tasks
web: gunicorn src.RemindMe.wsgi --log-file -
