#-*- coding: utf-8 -*-
#! /usr/bin/env python

'''
Created on Jan 29, 2016

@author: root
'''

from oslo_config import cfg
from oslo_log import log as logging

LOG = logging.getLogger(__name__)
CONF = cfg.CONF
DOMAIN = 'demo'


def prepare():
    """Prepare Oslo Logging (2 or 3 steps)

    Use of Oslo Logging involves the following:

    * logging.register_options
    * logging.set_defaults (optional)
    * logging.setup
    """

    # Required step to register common, logging and generic configuration
    # variables
    logging.register_options(CONF)

    # Optional step to set new defaults if necessary for
    # * logging_context_format_string
    # * default_log_levels
    #
    # These variables default to respectively:
    #
    #  import oslo_log
    #  oslo_log._options.DEFAULT_LOG_LEVELS
    #  oslo_log._options.log_opts[0].default
    #

    extra_log_level_defaults = [
        'dogpile=INFO',
        'routes=INFO'
        ]

    logging.set_defaults(
        default_log_levels=logging.get_default_log_levels() +
        extra_log_level_defaults)

    # Required setup based on configuration and domain
    logging.setup(CONF, DOMAIN)


if __name__ == '__main__':
    prepare()
    # NOTE: These examples do not demonstration Oslo i18n messages

    LOG.info("Welcome to Oslo Logging")
    LOG.debug("A debugging message")
    LOG.warning("A warning occured")
    LOG.error("An error occured")
    LOG.exception("An Exception occured")