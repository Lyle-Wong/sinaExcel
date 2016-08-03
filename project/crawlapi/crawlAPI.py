#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-14 19:46:04
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import json
import time
import requests
from settings.settings import *
from excelParse import excelUtil
from logger import logger


class Crawl:
    day_url = "/caches/task/exponent/bdi/day.json"
    week_url = "/caches/task/exponent/bdi/week.json"
    month_url = "/caches/task/exponent/bdi/month.json"

    def __init__(self):
        self.day_url = domain + self.day_url + \
            "?v=" + str(time.time() * 100000)
        self.week_url = domain + self.week_url + \
            "?v=" + str(time.time() * 100000)
        self.month_url = domain + self.month_url + \
            "?v=" + str(time.time() * 100000)

    @classmethod
    def get_data(cls, url):
        logger.info("Get URL: %s", url)
        resp = requests.get(url, headers=headers_xhr)
        return json.loads(resp.content.decode('utf-8'))

    def get_week_data(self):
        return self.get_data(self.week_url)

    def get_month_data(self):
        return self.get_data(self.month_url)

    def ex_rate(self, url):
        resp = requests.get(url, headers=headers_normal)
        content = resp.content.decode('gbk')
        return content

    def ex_rate_input(self):
        dollar_value = self.ex_rate(dollar_url).split(',')
        seurusd_value = self.ex_rate(seurusd_url).split(',')
        sgbpusd_value = self.ex_rate(sgbpusd_url).split(',')
        susdjpy_value = self.ex_rate(susdjpy_url).split(',')
        lowest = dollar_value[-4]
        highest = dollar_value[-5]
        yesterday_close = dollar_value[3]
        excelUtil.excel_write(excel_file_path, "（美联储）", "C", "3", lowest)
        excelUtil.excel_write(excel_file_path, "（美联储）", "C", "2", highest)
        excelUtil.excel_write(excel_file_path, "（美联储）",
                              "C", "4", yesterday_close)
        excelUtil.excel_write(excel_file_path, "（美联储）",
                              "C", "6", seurusd_value[3])
        excelUtil.excel_write(excel_file_path, "（美联储）",
                              "C", "10", sgbpusd_value[3])
        excelUtil.excel_write(excel_file_path, "（美联储）",
                              "C", "8", susdjpy_value[3])

    def bdi(self):
        data_month = self.get_month_data()
        # logger.info("data_month: %s", data_month)
        data_week = data_month[-5:]
        data_count = len(data_week)
        for num in range(data_count):
            logger.info("input data: %s", data_week[num])
            excelUtil.excel_write(excel_file_path, index_bdi, "C", str(
                2 * num + 3), data_week[num]['index'])
            excelUtil.excel_write(excel_file_path, index_bdi, "D", str(
                2 * num + 3), data_week[num]['date'])

        excelUtil.excel_write(excel_file_path, index_bdi,
                              "C", "2", data_month[-6]['index'])
        excelUtil.excel_write(excel_file_path, index_bdi,
                              "D", "2", data_month[-6]['date'])


if __name__ == '__main__':
    crawl = Crawl()
    crawl.bdi()
