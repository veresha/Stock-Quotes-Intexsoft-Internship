from src.celery_app.main import app


@app.task()
def add_info():
    pass
