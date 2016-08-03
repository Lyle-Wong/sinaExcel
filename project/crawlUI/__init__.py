#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-16 20:15:39
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from logger import logger
from settings import settings


def setup():
    rootPath = settings.root_path
    firefoxBin = FirefoxBinary(os.path.join(
        rootPath, r'Firefox\41\Mozilla Firefox\firefox.exe'))
    profile = webdriver.FirefoxProfile(
        os.path.join(rootPath, r'Firefox\41\profile'))
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)
    # profile.set_preference("javascript.enabled", False)
    # extensionList = [os.path.join(os.path.join(rootPath, r'Firefox\41\extensions'), extension) for extension in os.listdir(os.path.join(
    #     rootPath, r'Firefox\41\extensions'))]
    # for extension in extensionList:
    #     logger.info("Attempting to load extension: %s", extension.split('\\')[-1])
    #     profile.add_extension(extension=extension)
    # profile.set_preference("extensions.firebug.currentVersion", "2.0.13")
    logger.info("Initialize web browser...")
    try:
        browser = webdriver.Firefox(
            firefox_profile=profile, firefox_binary=firefoxBin)
    except Exception as ex:
        logger.exception(ex)
    return browser


def setup_chrome():
    rootPath = settings.root_path
    chrome_driver = os.path.join(rootPath, r'Chrome-bin\chromedriver.exe')
    os.environ['webdriver.chrome.driver'] = chrome_driver
    path = r'logs\no_binary_location.log'
    args = ['--verbose']
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=es')
    options.binary_location = os.path.join(rootPath, r'Chrome-bin\chrome.exe')
    try:
        browser = webdriver.Chrome(executable_path=chrome_driver, chrome_options=options,
                                   service_args=args, service_log_path=path)
    except Exception as ex:
        logger.exception(ex)
    return browser
