from src.celery_app.main import app
from src.app.main import get_info_from_yahoo, get_historical_data


@app.task
def add_historical_data():
    get_historical_data()
    return 'DONE'


@app.task
def add_info_from_yahoo():
    get_info_from_yahoo()
    return 'DONE'
