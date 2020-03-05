release: python manage.py migrate
web: python jj/manage.py runserver 0.0.0.0:$PORT
web: gunicorn base.wsgi --log-file -
