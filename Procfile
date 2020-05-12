release: python manage.py migrate
worker: python manage.py runscript src.clock & python manage.py process_tasks
web: gunicorn wsgi --log-file -
