!#/bin/bash

until pg_isready -h db -p 5432 -U user; do
  echo "Waiting for PostgreSQL..."
  sleep 2
done

python manage.py migrate

export DJANGO_SUPERUSER_USERNAME="corpay_user"
export DJANGO_SUPERUSER_EMAIL="takehome@corpay.com"
export DJANGO_SUPERUSER_PASSWORD="s@mplePassword"

python manage.py createsuperuser --noinput

python manage.py runserver