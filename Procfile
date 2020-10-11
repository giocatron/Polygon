release: python manage.py migrate --no-input
web: gunicorn --bind :$PORT --workers 4 --worker-class uvicorn.workers.UvicornWorker polygon.asgi:application
celeryworker: celery worker -A polygon.celeryconf:app --loglevel=info -E
