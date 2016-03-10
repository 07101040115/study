#!/usr/bin/env python
# coding=utf-8

'''
Created on Dec 19, 2015
@author: root
'''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange = 'logs', exchange_type = 'fanout' )

message = ''.join(sys.argv[1:]) or 'info: Hello world!'

channel.basic_publish(exchange = 'logs', routing_key = '', body = message)

print '[x] Send %r' % (message,)

connection.close()