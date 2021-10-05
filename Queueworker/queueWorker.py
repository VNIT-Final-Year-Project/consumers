# consumer.py
# Consume RabbitMQ queue
import threading

import pika
import json
from Queueworker.fastComputation.fastComputation import fastComputation

class Queueworker():
    def __init__(self):
        self.producer_q = []
        self.consumer_q = []
        self.threadlock = threading.Lock()

    def consume(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials("user", "password")))
        channel = connection.channel()

        def callback(ch, method, properties, body):
            body = body.decode('utf-8')
            body = json.loads(body)
            self.consumer_q.append(body)

        channel.basic_consume(queue="Server1", on_message_callback=callback, auto_ack=True)
        channel.start_consuming()

    def produce(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password')))
        channel = connection.channel()

        while(True):
            if(len(self.producer_q)>0):
                element = self.producer_q.pop(0)
                print(element)
                json_string = json.dumps(element)
                channel.basic_publish(exchange='output_exchange',
                                      routing_key='output', body=json_string)

    def calculate(self):
        while(True):
            if(self.threadlock.acquire() and len(self.consumer_q)>0):
                print('calculating')
                element = self.consumer_q.pop(0)
                self.threadlock.release()
                X = element[0]
                Y = element[1]
                result = fastComputation.lcs(X,Y)
                result = [element[2],result]
                self.producer_q.append(result)



