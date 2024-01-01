#!/bin/sh

until python ./manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

# Apply database migrations
python manage.py flush --no-input
python manage.py migrate

exec gunicorn swiftview_analytics.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4