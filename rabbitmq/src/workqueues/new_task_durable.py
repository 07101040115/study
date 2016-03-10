#! /usr/bin/env python 

import sys
import pika

if len(sys.argv) < 2:
    print 'Usage: '
    sys.exit(0)

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))

channel = connection.channel()

channel.queue_declare(queue = 'task_queue', durable = True)

count = int(sys.argv[1])

for i in range(0, count):
    message = '%s measage %s' % (i, '.'*i)
    
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(
                        delivery_mode = 2, # make message persistent
                        ))

    print " [x] Sent %s" % message

connection.close()