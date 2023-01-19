from src.celery_app.main import app
from src.app.main import get_info
from src.config import *


@app.task()
def add_info():
    url = BASE_URL
    get_info(url=url)
