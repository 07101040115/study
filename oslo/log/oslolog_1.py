#-*- coding: utf-8 -*-
#! /usr/bin/env python

'''
Created on Jan 29, 2016

@author: root
'''

from oslo_config import cfg
from oslo_log import log as logging

DOMAIN = "demo"

LOG = logging.getLogger(__name__)
CONF = cfg.CONF

def prepare():
    logging.register_options(CONF)
    


logging.register_options(CONF)
logging.setup(CONF, DOMAIN)

prepare()
# Oslo Logging uses INFO as default
LOG.info("Oslo Logging")
LOG.warning("Oslo Logging")
LOG.error("Oslo Logging")


print logging.get_default_log_levels()