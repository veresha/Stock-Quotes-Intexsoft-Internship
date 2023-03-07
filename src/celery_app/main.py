from celery import Celery
from src.config import RABBITMQ_BROKER, RABBITMQ_BACKEND, CELERY_BEAT_NAME, TIMEZONE


app = Celery(
    CELERY_BEAT_NAME,
    broker=RABBITMQ_BROKER,
    backend=RABBITMQ_BACKEND,
    include="src.celery_app.tasks"
)
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-info-from-api': {
        'task': 'src.celery_app.tasks.sync.add_historical_data',
        'schedule': 500.0 # кронлаб и енв
    },
}

# app.conf.beat_schedule = {
#     'add-info-from-api': {
#         'task': 'src.celery_app.tasks.sync.add_info_from_yahoo',
#         'schedule': 30.0
#     },
# }

app.conf.timezone = TIMEZONE
