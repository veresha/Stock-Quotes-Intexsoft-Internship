from celery import Celery
from src.config import RABBITMQ_BROKER, RABBITMQ_BACKEND


app = Celery(
    'beater',
    broker=RABBITMQ_BROKER,
    backend=RABBITMQ_BACKEND,
    include="src.celery_app.tasks"
)
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-info-every-5-minutes': {
        'task': 'src.celery_app.tasks.sync.add_info',
        'schedule': 60.0
    },
}
app.conf.timezone = 'UTC'
