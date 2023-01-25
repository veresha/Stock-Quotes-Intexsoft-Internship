import os


BASE_URL = os.getenv('BASE_URL', 'https://finnhub.io/api/v1/quote')
API_KEY = os.getenv('API_KEY', 'cf83dgqad3i8qmbtig60cf83dgqad3i8qmbtig6g')

MONGO_INITDB_ROOT_USERNAME = os.getenv('MONGO_INITDB_ROOT_USERNAME', 'root')
MONGO_INITDB_ROOT_PASSWORD = os.getenv('MONGO_INITDB_ROOT_PASSWORD', 'example')
MONGO_INITDB_HOST = os.getenv('MONGO_INITDB_HOST', 'mongodb://172.22.0.2:27017/')

RABBITMQ_BROKER = os.getenv('RABBITMQ_BROKER', 'amqp://guest:guest@rabbitmq:5672/')
RABBITMQ_BACKEND = os.getenv('RABBITMQ_BACKEND', 'rpc://')
