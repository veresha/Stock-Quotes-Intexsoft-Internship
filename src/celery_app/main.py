from celery import Celery

import src.config as c


app = Celery(
    c.CELERY_BEAT_NAME,
    broker=c.RABBITMQ_BROKER,
    backend=c.RABBITMQ_BACKEND,
    include="src.celery_app.tasks"
)
app.autodiscover_tasks()
app.conf.timezone = c.TIMEZONE

app.conf.beat_schedule = {
    'add-info-from-api': {
        'task': 'src.celery_app.tasks.sync.add_historical_data',
        'schedule': c.PERIOD
    },
}
