#!/usr/bin/env bash

set -o errexit

pip -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

