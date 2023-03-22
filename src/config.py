import os


BASE_URL = os.getenv('BASE_URL', 'https://finnhub.io/api/v1/quote')
API_KEY = os.getenv('API_KEY', 'cf83dgqad3i8qmbtig60cf83dgqad3i8qmbtig6g')

CELERY_BEAT_NAME = os.getenv('CELERY_BEAT_NAME', 'beater')
KAFKA_SERVER = os.getenv('KAFKA_SERVER', 'kafka:9092')
KAFKA_TOPIC_NAME = os.getenv('KAFKA_TOPIC_NAME', 'quotes')

RABBITMQ_BROKER = os.getenv('RABBITMQ_BROKER', 'amqp://guest:guest@rabbitmq:5672/')
RABBITMQ_BACKEND = os.getenv('RABBITMQ_BACKEND', 'rpc://')
TIMEZONE = os.getenv('TIMEZONE', 'UTC')
PERIOD = 500

companies_tpl = ('AAPL', 'AMZN', 'TSLA', 'MSFT', 'GOOG',)
