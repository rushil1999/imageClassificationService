#!/usr/bin/env bash
# exit on error
set -o errexit

poetry lock --no-update

pip install -r requirements.txt

python manage.py collectstatic --no-input