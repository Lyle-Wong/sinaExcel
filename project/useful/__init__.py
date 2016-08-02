#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-16 20:14:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import datetime


class TimeUtil(object):
    oneday = datetime.timedelta(days=1)
    current_date = str(datetime.date.today()).replace('-', '/')
    yesterday = str(datetime.date.today() - oneday).replace('-', '/')
    beforeyesterday = str(datetime.date.today() -
                          oneday - oneday).replace('-', '/')
    prebeforeyesterday = str(datetime.date.today() -
                             oneday - oneday - oneday).replace('-', '/')

    @classmethod
    def judge_display_date(cls, date):
        if date.find(cls.current_date) == 0:
            return "today"
        elif date.find(cls.yesterday) == 0:
            return "yesterday"
        elif date.find(cls.beforeyesterday) == 0:
            return "beforeyesterday"
        elif date.find(cls.prebeforeyesterday) == 0:
            return "prebeforeyesterday"
        else:
            return "unknown date"
