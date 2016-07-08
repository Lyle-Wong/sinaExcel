#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-17 10:58:55
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import sys
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
from settings import settings
from logger import logger
from excelParse import excelUtil
from . import setup


class CrawlUI:

    def __init__(self):
        self.browser = setup()
        self.browser.implicitly_wait(30)
        self.browser.maximize_window()

    def get_diniw(self, url):
        self.action = ActionChains(self.browser)
        logger.info("Open URL: %s", url)
        self.browser.get(url)
        self.browser.implicitly_wait(30)
        canvasElement = self.browser.find_element_by_xpath(
            settings.canvas_Xpath)
        logger.info("canvas is present: %s", canvasElement.is_displayed())
        self.action.move_to_element_with_offset(
            canvasElement, 600, 200).perform()
        highest_value = self.browser.find_element_by_xpath(
            settings.highest_XPath).text
        lowest_value = self.browser.find_element_by_xpath(
            settings.lowest_XPath).text
        closed_value = self.browser.find_element_by_xpath(
            settings.closed_XPath).text
        excelUtil.excel_write(settings.excel_file_path, settings.excel_first_sheet,
                              "C", "2", highest_value.split('(')[0])
        excelUtil.excel_write(settings.excel_file_path, settings.excel_first_sheet,
                              "C", "3", lowest_value.split('(')[0])
        excelUtil.excel_write(settings.excel_file_path, settings.excel_first_sheet,
                              "C", "4", closed_value.split('(')[0])
        excelUtil.excel_write(settings.excel_file_path, settings.excel_first_sheet,
                              "C", "5", closed_value.split('(')[1].split(')')[0])

    def ex_sub_rate(self, url, basePosition):
        self.action = ActionChains(self.browser)
        logger.info("Open URL: %s", url)
        self.browser.get(url)
        daily_k_Element = self.browser.find_element_by_xpath(
            settings.daily_k_Xpath)
        self.action.click(daily_k_Element).perform()
        daily_k_canvasElement = self.browser.find_element_by_xpath(
            settings.canvas_Xpath)
        self.action.move_to_element_with_offset(
            daily_k_canvasElement, 600, 200).perform()
        closed_value = self.browser.find_element_by_xpath(
            settings.closed_XPath).text
        excelUtil.excel_write(settings.excel_file_path, settings.excel_first_sheet,
                              "C", str(basePosition), closed_value.split('(')[0])
        excelUtil.excel_write(settings.excel_file_path, settings.excel_first_sheet,
                              "C", str(basePosition + 1), closed_value.split('(')[1].split(')')[0])

    def american_stock(self, url, basePosition):
        self.action = ActionChains(self.browser)
        logger.info("Open URL: %s", url)
        self.browser.get(url)
        daily_k_Element = self.browser.find_element_by_xpath(
            settings.stock_daily_k_Xpath)
        self.action.click(daily_k_Element).perform()
        daily_k_canvasElement = self.browser.find_element_by_xpath(
            settings.canvas_Xpath)
        logger.info("canvas found: %s", daily_k_canvasElement.is_displayed())
        self.action.move_to_element_with_offset(
            daily_k_canvasElement, 620, 150).perform()
        closed_value = self.browser.find_element_by_xpath(
            settings.stock_closed_XPath).text
        logger.info("closed Value: %s", closed_value)
        excelUtil.excel_write(settings.excel_file_path, settings.excel_first_sheet,
                              "C", str(basePosition), closed_value.split('(')[0])
        excelUtil.excel_write(settings.excel_file_path, settings.excel_first_sheet,
                              "C", str(basePosition + 1), closed_value.split('(')[1].split(')')[0])

    def ex_rate(self):
        self.get_diniw(settings.dollar_index_url)
        self.ex_sub_rate(settings.eurusd_url, 6)
        self.ex_sub_rate(settings.usdjpy_url, 8)
        self.ex_sub_rate(settings.gbpusd_url, 10)
        self.american_stock(settings.inx_url, 13)
        self.american_stock(settings.dji_url, 15)
        self.american_stock(settings.ixic_url, 17)


if __name__ == '__main__':
    path = os.path.abspath(sys.path[0])
    logger.info("Current working path: %s", path)
    crawlUI = CrawlUI()
    crawlUI.ex_rate(settings.dollar_index_url)