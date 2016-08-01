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

    def eup_ex_sub_rate(self, url, basePosition):
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
        excelUtil.excel_write(settings.excel_file_path, settings.excel_second_sheet,
                              "C", str(basePosition), closed_value.split('(')[0])
        excelUtil.excel_write(settings.excel_file_path, settings.excel_second_sheet,
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

    def american_debt(self, url):
        logger.info("Open URL: %s", url)
        self.browser.get(url)
        valueYesterdayElements = self.browser.find_elements_by_xpath(
            settings.american_debt_yesterday_xpath)
        valueBeforeElements = self.browser.find_elements_by_xpath(
            settings.american_debt_before_xpath)
        yesterdayValues = [i.text for i in valueYesterdayElements][7:]
        beforeValues = [i.text for i in valueBeforeElements][7:]
        for i in range(len(yesterdayValues)):
            excelUtil.excel_write(settings.excel_file_path,
                                  settings.excel_first_sheet, "C", str(2 * i + 29), yesterdayValues[i])
            excelUtil.excel_write(settings.excel_file_path, settings.excel_first_sheet, "C", str(
                2 * i + 30), format((float(yesterdayValues[i]) - float(beforeValues[i])) / float(yesterdayValues[i]), '.3%'))

    def europe_stock(self, url):
        self.browser.get(url)
        value = self.browser.find_element_by_xpath(
            settings.dax_xpath_value).text
        rate = self.browser.find_element_by_xpath(settings.dax_xpath_rate).text
        excelUtil.excel_write(settings.excel_file_path,
                              settings.excel_first_sheet, "C", "22", value)
        excelUtil.excel_write(settings.excel_file_path,
                              settings.excel_first_sheet, "C", "23", rate)
        excelUtil.excel_write(settings.excel_file_path,
                              settings.excel_second_sheet, "C", "13", value)
        excelUtil.excel_write(settings.excel_file_path,
                              settings.excel_second_sheet, "C", "14", rate)
        value = self.browser.find_element_by_xpath(
            settings.cac_xpath_value).text
        rate = self.browser.find_element_by_xpath(settings.cac_xpath_rate).text
        excelUtil.excel_write(settings.excel_file_path,
                              settings.excel_first_sheet, "C", "24", value)
        excelUtil.excel_write(settings.excel_file_path,
                              settings.excel_first_sheet, "C", "25", rate)
        excelUtil.excel_write(settings.excel_file_path,
                              settings.excel_second_sheet, "C", "15", value)
        excelUtil.excel_write(settings.excel_file_path,
                              settings.excel_second_sheet, "C", "16", rate)
        value = self.browser.find_element_by_xpath(
            settings.ukx_xpath_value).text
        rate = self.browser.find_element_by_xpath(settings.ukx_xpath_rate).text
        excelUtil.excel_write(settings.excel_file_path,
                              settings.excel_first_sheet, "C", "26", value)
        excelUtil.excel_write(settings.excel_file_path,
                              settings.excel_first_sheet, "C", "27", rate)
        excelUtil.excel_write(settings.excel_file_path,
                              settings.excel_second_sheet, "C", "17", value)
        excelUtil.excel_write(settings.excel_file_path,
                              settings.excel_second_sheet, "C", "18", rate)

    # 大宗商品价格
    def commodity_price(self, url, basePosition):
        self.action = ActionChains(self.browser)
        logger.info("Open URL: %s", url)
        self.browser.get(url)
        daily_k_Element = self.browser.find_element_by_xpath(
            settings.commodity_xpath)
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
        self.eup_ex_sub_rate(settings.eurusd_url, 2)
        self.eup_ex_sub_rate(settings.eurrgbp_url, 4)
        self.eup_ex_sub_rate(settings.eurchf_url, 6)
        self.eup_ex_sub_rate(settings.eurjpy_url, 8)
        self.american_stock(settings.inx_url, 13)
        self.american_stock(settings.dji_url, 15)
        self.american_stock(settings.ixic_url, 17)
        self.commodity_price(settings.wti_url, 40)
        self.europe_stock(settings.europe_stock)
        self.american_debt(settings.american_debt)
        self.browser.quit()


if __name__ == '__main__':
    path = os.path.abspath(sys.path[0])
    logger.info("Current working path: %s", path)
    crawlUI = CrawlUI()
    crawlUI.ex_rate(settings.dollar_index_url)
