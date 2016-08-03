#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-15 13:23:09
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import time
import threading
import tkinter as tk
import tkinter.font as font
from crawlapi import crawlAPI
from crawlUI import crawlUI
from useful import qiushi
from logger import logger
from settings import settings


class CrawlApplication(object):
    """docstring for CrawlApplication"""

    def __init__(self, title=" Please Enjoying", width=350, height=500):
        self.w = width
        self.h = height
        self.root = tk.Tk(className=title)

    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int((ws / 2) - (self.w / 2))
        y = int((hs / 2) - (self.h / 2))
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

    def UI_func(self, is_use_chrome):
        crawl = crawlUI.CrawlUI(is_use_chrome)
        try:
            crawl.ex_rate()
        except Exception as ex:
            logger.exception(ex)

    def API_func(self):
        crawl = crawlAPI.Crawl()
        crawl.bdi()
        # crawl.ex_rate_input()

    def new_thread1(self):
        t = threading.Thread(target=self.API_func)
        t.start()

    def new_thread2(self, is_use_chrome):
        t = threading.Thread(target=self.UI_func, args=(is_use_chrome,))
        t.start()

    def submitBtn(self):
        helv36 = font.Font(family='Microsoft YaHei', size=12, weight='bold')
        helv8 = font.Font(family='Microsoft YaHei', size=9)
        font_joke = font.Font(family='Microsoft YaHei', size=12)
        self.btnSer1 = tk.Button(self.root,
                                 command=self.new_thread1,
                                 width=30,
                                 height=2,
                                 text="通过 API 爬取数据",
                                 font=helv36
                                 )
        tk.Label(self.root).pack(padx=20, side='top')
        self.btnSer2 = tk.Button(self.root,
                                 command=lambda: self.new_thread2(is_use_chrome.get()),
                                 width=30,
                                 height=2,
                                 text="通过 UI 爬取数据",
                                 font=helv36
                                 )
        self.btnSer1.pack(padx=20, side='top')
        tk.Label(self.root).pack(padx=10, side='top')
        self.btnSer2.pack(padx=20, side='top')
        tk.Label(self.root).pack(padx=10, side='top')
        is_use_chrome = tk.IntVar()
        self.cb = tk.Checkbutton(self.root, text='使用Chrome浏览器', variable=is_use_chrome, font=helv8)
        self.cb.pack(padx=20, side='top')
        tk.Label(self.root).pack(padx=20, side='top')
        tk.Message(self.root,
                   text=qiushi.get_joke(),
                   # text = joke,
                   width=300,
                   font=font_joke
                   ).pack(padx=20, side='top')
        tk.Label(self.root, text="Powered by Lyle").pack(
            padx=20, side="bottom")

    def loop(self):
        self.root.resizable(False, False)
        self.submitBtn()
        self.center()
        self.root.mainloop()


if __name__ == '__main__':
    app = CrawlApplication()
    app.loop()
