#-*- coding: utf-8 -*-
#! /usr/bin/env python

'''
Created on Jan 28, 2016

@author: root
'''


from oslo_config import cfg
import os

opts = [
        cfg.StrOpt('state_path',
                   default = os.path.join(os.path.dirname(__file__), '../'),
                   help = 'Top-level directory for maintaining nova state.'),
        cfg.StrOpt('sqlite_db',
                   default='nova.sqlite',
                   help='File name for SQLite'
                   ),
        cfg.StrOpt('sql_connection',
                   default='sqlite:///$state_path/$sqlite_db',
                   help='Connection string for SQL database'
                   ),
        ]


conf = cfg.ConfigOpts()
conf.register_cli_opts(opts)
print conf.sql_connection

conf_1 = cfg.ConfigOpts()
conf_1.register_cli_opts(opts)
print conf_1.state_path
conf_1(default_config_files=['./test.conf'])
print conf_1.state_path


