#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-14 19:50:08
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import sys
import time


headers_xhr = {
    "Accept-Encoding": "gzip",
    "Cache-Control": "max-age=0",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
    "Accept-Language":  "zh-CN,zh;q=0.8,en;q=0.6,en-US;q=0.4,zh-TW;q=0.2",
    "Connection":  "keep-alive",
    "Accept-Encoding":  "gzip, deflate",
    "Referer": "http://www.cnss.com.cn/exponent/bdi/?type=bdi",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "X-Requested-With": "XMLHttpRequest"
}

headers_normal = {
    "Accept-Encoding": "gzip",
    "Cache-Control": "max-age=0",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
    "Accept-Language":  "zh-CN,zh;q=0.8,en;q=0.6,en-US;q=0.4,zh-TW;q=0.2",
    "Connection":  "keep-alive",
    "Accept-Encoding":  "gzip, deflate",
    "Referer": "http://www.cnss.com.cn/exponent/bdi/?type=bdi",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

domain = "http://www.cnss.com.cn"

desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
root_path = os.getcwd()

excel_name = "金融市场反应.xlsx"

excel_file_path = os.path.join(desktop_path, excel_name)

excel_first_sheet = "（美联储）"


# 波罗的海
index_bdi = "（波罗的海）"

# 美元
dollar_url = "http://hq.sinajs.cn/rn=" + \
    str(int(time.time() * 1000)) + "list=DINIW"

#ex_rate_url = "http://hq.sinajs.cn/rn="+str(int(time.time()*1000))+"list=fx_seurusd,fx_sgbpusd,fx_susdjpy,fx_saudusd,fx_susdchf,fx_susdcad,fx_snzdusd,fx_susdhkd,fx_susdrub,fx_susdkrw,fx_susdthb,fx_susdsgd"

# 欧元美元
seurusd_url = "http://hq.sinajs.cn/rn=" + \
    str(int(time.time() * 1000)) + "list=fx_seurusd"

# 英镑美元
sgbpusd_url = "http://hq.sinajs.cn/rn=" + \
    str(int(time.time() * 1000)) + "list=fx_sgbpusd"

# 美元日元
susdjpy_url = "http://hq.sinajs.cn/rn=" + \
    str(int(time.time() * 1000)) + "list=fx_susdjpy"


canvas_Xpath = "//div[contains(@id, 'mainarea')]"

# 汇率
dollar_index_url = "http://finance.sina.com.cn/money/forex/hq/DINIW.shtml"
eurusd_url = "http://finance.sina.com.cn/money/forex/hq/EURUSD.shtml"
usdjpy_url = "http://finance.sina.com.cn/money/forex/hq/USDJPY.shtml"
gbpusd_url = "http://finance.sina.com.cn/money/forex/hq/GBPUSD.shtml"
EURUSD_Xpath = ".//*[@id='zphl_list']/tr[1]/td[1]/a"
GBPUSD_Xpath = ".//*[@id='zphl_list']/tr[2]/td[1]/a"
daily_k_Xpath = "//div[@class='hqH5_nav']//li[@data-action='kd']"

highest_XPath = ".//*[@id='hqH5_content']//table/tbody/tr[3]/td/span"
lowest_XPath = ".//*[@id='hqH5_content']//table/tbody/tr[4]/td/span"
closed_XPath = ".//*[@id='hqH5_content']//table/tbody/tr[5]/td/span"

# 标普500
inx_url = "http://stock.finance.sina.com.cn/usstock/quotes/.INX.html"

# 道琼斯工业平均
dji_url = "http://stock.finance.sina.com.cn/usstock/quotes/.DJI.html"

# 纳斯达克综合
ixic_url = "http://stock.sina.com.cn/usstock/quotes/.IXIC.html"
stock_daily_k_Xpath = "//div[@class='kke_menus_tab_edage']//div[@data-view='kd']/a"
stock_closed_XPath = "//table/tbody/tr[5]/td/span"


# 每一页下载等待时间
wait_sec = 1