from src.celery_app.main import app
from src.app.main import get_info


@app.task
def add_info():
    print('Выполнение задачи')
    get_info()
