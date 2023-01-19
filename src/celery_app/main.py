from celery import Celery

app = Celery()

app.conf.beat_schedule = {
    'add-info-every-5-minutes': {
        'task': 'tasks.add_info',
        'schedule': 300.0
    },
}
app.conf.timezone = 'UTC'
