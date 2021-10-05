# consumer.py
# Consume RabbitMQ queue

import pika
import json
from Queueworker.fastComputation.fastComputation import fastComputation

class Queueworker():
    def __init__(self):
        self.producer_q = []
        self.consumer_q = []

    def consume(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials("user", "password")))
        channel = connection.channel()

        def callback(ch, method, properties, body):
            body = body.decode('utf-8')
            body = json.loads(body)
            self.consumer_q.append(body)

        channel.basic_consume(queue="server1", on_message_callback=callback, auto_ack=True)
        channel.start_consuming()

    def produce(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password')))
        channel = connection.channel()

        while(True):
            if(len(self.producer_q)>0):
                element = self.producer_q.pop(0)
                print(element)
                channel.basic_publish(exchange='output_exchange',
                                      routing_key='output', body=bytes(element))

    def calculate(self):
        while(True):
            if(len(self.consumer_q)>0):
                element = self.consumer_q.pop(0)
                X = element[0]
                Y = element[1]
                result = fastComputation.lcs(X,Y)
                self.producer_q.append(result)


