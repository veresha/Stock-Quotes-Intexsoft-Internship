from src.app.kafka_producer import Producer


def publish_message(data):
    producer_instance = Producer()
    try:
        producer_instance.publish_message(data)
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))
