import json
from kafka import KafkaProducer
from src.config import KAFKA_TOPIC_NAME, KAFKA_SERVER


def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(
            bootstrap_servers=[KAFKA_SERVER],
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer


def publish_message(data):
    producer_instance = connect_kafka_producer()
    try:
        producer_instance.send(KAFKA_TOPIC_NAME, value=data)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))
