#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-15 13:59:53
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import requests
import random
from bs4 import BeautifulSoup
from settings.settings import headers_normal
from logger import logger


def get_joke():
	try:
		url = "http://caodan.org/page/{num}".format(num= str(random.randint(1, 1001)))
		logger.info("Get info from URL:%s", url)
		page = requests.get(url, headers=headers_normal)
		soup = BeautifulSoup(page.content, 'html.parser')
		logger.info("get joke....")
		contents = soup.find_all("div", attrs = {"class":"content"})
		joke = contents[0].find_all("blockquote")[0].text.encode('utf-8')
		return joke.decode('utf-8')
	except:
		return "获取每日一句失败。。。"



