#!/usr/bin/env python
# encoding: utf-8
"""
@author: xingrong.peng
@file: logger.py
@time: 2023/2/22 下午4:22
"""

import os.path
import sys
import logging
from config import home_path, is_py2
from loghandler import MidnightRotatingFileHandler

LOGGER_NAME = "SelDis"
robot_log_path = "/userdata/SelDis_logs/"


class SingleLevelFilter(logging.Filter):
    """ Filters out on single message levels

    """

    def __init__(self, level, accept=True):
        super(SingleLevelFilter, self).__init__()
        self.levelno = level
        self.accept = accept

    def filter(self, record):
        if self.accept:
            return record.levelno == self.levelno
        return record.levelno != self.levelno


class Logger(object):
    """ The logger for tracing logger

    """
    logger = None

    def __init__(self, log_root):
        self.log_root = log_root

        self.log = logging.getLogger(LOGGER_NAME)
        self.log.setLevel(logging.DEBUG)

        self.log_info = MidnightRotatingFileHandler(os.path.join(self.log_root, 'log'))
        self.log_info.setLevel(logging.INFO)

        self.log_console = logging.StreamHandler(stream=sys.stdout)
        self.log_console.addFilter(SingleLevelFilter(logging.ERROR, False))
        self.log_console.setLevel(logging.DEBUG)
        self.log_console_error = logging.StreamHandler(stream=sys.stderr)
        self.log_console_error.setLevel(logging.ERROR)

        timestamp_fmt = "[%(asctime)s.%(msecs)03d" + "] %(levelname)-6s %(threadName)-12s <%(filename)s:+%(lineno)d> %(" \
                                                     "message)s "

        self.formatter_info = logging.Formatter(timestamp_fmt, datefmt="%Y-%m-%dT%H:%M:%S")
        self.log_info.setFormatter(self.formatter_info)
        self.log_console.setFormatter(self.formatter_info)

        self.log.addHandler(self.log_console)
        self.log.addHandler(self.log_console_error)
        self.log.addHandler(self.log_info)

    @classmethod
    def get_instance(cls):
        if Logger.logger is None:
            log_path = os.path.join(home_path, 'SelDis_logs')
            if not os.path.exists(log_path):
                os.makedirs(log_path)
            if is_py2:
                log_path = robot_log_path
                if not os.path.exists(log_path):
                    os.mkdir(log_path)
            Logger.logger = Logger(log_path)
        return Logger.logger.log

