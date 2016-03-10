#! /usr/bin/env python 

import sys
import pika

if len(sys.argv) < 2:
    print 'Usage: '
    sys.exit(0)

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))

channel = connection.channel()

channel.queue_declare(queue = 'hello')

count = int(sys.argv[1])

for i in range(0, count):
    message = '%s measage %s' % (i, '.'*i)
    
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)

    print " [x] Sent %s" % message

connection.close()