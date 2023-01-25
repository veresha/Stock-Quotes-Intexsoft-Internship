#! /bin/sh

celery -A src.celery_app.main beat -l INFO

