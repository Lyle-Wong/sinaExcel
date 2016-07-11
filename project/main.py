#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-16 20:16:30
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import sys
import shutil
from UI import uicore
from logger import logger
from settings.settings import *


if __name__ == '__main__':
    logger.info("copy file to desktop...")
    logger.info("working dir: %s", os.getcwd())
    shutil.copy(os.getcwd() + "\\" + excel_name, excel_file_path)
    app = uicore.CrawlApplication()
    app.loop()
