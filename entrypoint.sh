#!/usr/bin/env bash
set -e
echo "Waiting for PostgreSQL at $POSTGRES_HOST:$POSTGRES_PORT ..."
until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do sleep 0.5; done
echo "PostgreSQL is up."

cd /app/backend
python manage.py migrate --noinput
python manage.py collectstatic --noinput

if [ "$DJANGO_DEBUG" = "1" ]; then
  exec python manage.py runserver 0.0.0.0:8000
else
  exec gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 120
fi
