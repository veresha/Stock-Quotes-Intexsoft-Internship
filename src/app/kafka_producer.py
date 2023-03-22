import json
from kafka import KafkaProducer
from src.config import KAFKA_SERVER, KAFKA_TOPIC_NAME
from src.app.singleton import Singleton


class Producer(metaclass=Singleton):

    __connection = None

    def __init__(self):
        self.__connection = KafkaProducer(bootstrap_servers=[KAFKA_SERVER],
                                          value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    def publish_message(self, data):
        self.__connection.send(KAFKA_TOPIC_NAME, value=data)
        self.__connection.flush()
