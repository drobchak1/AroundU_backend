release: python manage.py migrate "events", "users"
web: gunicorn AroundU.wsgi --pythonpath=AroundU --log-file -