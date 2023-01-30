from src.celery_app.main import app
from src.app.main import get_info


@app.task
def add_info():
    get_info()
    return 'DONE'
