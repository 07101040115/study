#!/usr/bin/env python
# coding=utf-8

'''
Created on Dec 19, 2015
@author: root
'''

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host = 'localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(exclusive = True)
queue_name = result.method.queue

channel.queue_bind(exchange ='logs', queue=queue_name)

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print '[X] %r' % (body,)
    
channel.basic_consume(consumer_callback=callback, queue=queue_name, no_ack=True)

channel.start_consuming()