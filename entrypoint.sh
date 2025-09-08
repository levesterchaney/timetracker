#!/bin/bash

python manage.py migrate

export DJANGO_SUPERUSER_USERNAME="corpay_user"
export DJANGO_SUPERUSER_EMAIL="takehome@corpay.com"
export DJANGO_SUPERUSER_PASSWORD="s@mplePassword"

python manage.py createsuperuser --noinput

python manage.py runserver 0.0.0.0:8000