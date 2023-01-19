from celery import Celery

app = Celery()

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-5-minutes': {
        'task': 'tasks.add',
        'schedule': 300.0
    },
}
app.conf.timezone = 'UTC'
