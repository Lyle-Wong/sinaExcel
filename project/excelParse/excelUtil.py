#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-15 21:48:22
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import sys
import openpyxl
from logger import logger


def excel_write(filepath, worksheet, row, column, value):
    try:
        logger.info("excel path: %s, write location(%s, %s) and value is: %s",
                    filepath, row, column, value)
        xfile = openpyxl.load_workbook(filepath)
        sheet = xfile.get_sheet_by_name(worksheet)
        sheet[row + column] = value
        xfile.save(filepath)
    except Exception as ex:
        logger.exception(ex)
