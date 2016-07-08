#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-16 10:26:30
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import sys
import json
import logging
from settings import settings


def logger_singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@logger_singleton
class MyLogger(object):
    def __init__(self):
        pass

    @staticmethod
    def setup_logging():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # create a file handler

        log_path = os.path.join(settings.root_path, 'logs')
        if not os.path.isdir(log_path):
            os.mkdir(log_path)

        handler = logging.FileHandler(log_path + "/" +__name__ + '.log')
        handler.setLevel(logging.INFO)

        # create a logging format

        handlerStream = logging.StreamHandler()
        handlerStream.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        handlerStream.setFormatter(formatter)

        # add the handlers to the logger

        logger.addHandler(handler)
        logger.addHandler(handlerStream)
        return logger

logger = MyLogger().setup_logging()


#from . import checkTag
