import pika

class Meter(object):
    def __init__(self, queue='powerValues'):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue='powerValues')
        self.queue = queue

    def publish(self, payload):
        self._channel.basic_publish(exchange='', routing_key='powerValues', body=payload)   
        print(f"sent message: {payload}")

    def basic_consumer(self, queue, callback, ack):
        self._channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=ack)
        print("Waiting for messages..")
        self._channel.start_consuming()


        



