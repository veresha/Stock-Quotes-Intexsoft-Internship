from celery import Celery
from src.config import *


app = Celery(
    'beater',
    broker=RABBITMQ_BROKER,
    backend=RABBITMQ_BACKEND,
    include="src.celery_app.tasks"
)
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-info-every-5-minutes': {
        'task': 'tasks.add_info',
        'schedule': 30.0
    },
}
app.conf.timezone = 'UTC'
