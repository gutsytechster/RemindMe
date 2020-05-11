release: python manage.py migrate
worker: python manage.py process_tasks
web: gunicorn wsgi --log-file -
