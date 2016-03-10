#-*- coding: utf-8 -*-
#! /usr/bin/env python

'''
Created on Jan 28, 2016

@author: root
'''

from oslo_config import cfg

conf = cfg.ConfigOpts()

rabbit_group = cfg.OptGroup(name = 'rabbit', title = 'RabbitMQ options')
rabbit_host_opt = cfg.StrOpt('host', default='localhost', help='IP/hostname to listen on.')
rabbit_port_opt = cfg.PortOpt('port', default=1245, help='Port number to listen on.')

def register_rabbit_opts(conf):
    conf.register_group(rabbit_group)
    conf.register_opt(rabbit_host_opt, group=rabbit_group)
    conf.register_opt(rabbit_port_opt, group=rabbit_group)
    
    
register_rabbit_opts(conf)
print conf.rabbit.host
print conf.rabbit.port


