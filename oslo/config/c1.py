#-*- coding: utf-8 -*-
#! /usr/bin/env python

'''
Created on Jan 28, 2016

@author: root
'''

from oslo_config import cfg
from oslo_config import types
import sys

PortType = types.Integer(1, 65535)

common_opts = [
               cfg.StrOpt('bind_host',
                          default = '0.0.0.0',
                          help = 'IP address to listen on.'),
               cfg.Opt('bind_port',
                       type=PortType,
                       default=9292,
                       help='Port number to listen on.'
                       )
               
               ]


enabled_apis_opt = cfg.ListOpt('enables_apis', 
                               default = ['ec2', 'osapi_compute'],
                               help = 'List of APIs to enable by default.'
                               )

DEFAULT_EXTENSIONS = [
                      'nova.api.openstack.compute.contrib.standrd_extensios'
                      ]

osapi_compute_extension_opt = cfg.MultiStrOpt('osapi_compute_extension',
                                              default = DEFAULT_EXTENSIONS
                                              )


CONF = cfg.ConfigOpts()
CONF.register_cli_opts(common_opts)


CONF(sys.argv[1:])

print CONF.bind_host
print CONF.bind_port