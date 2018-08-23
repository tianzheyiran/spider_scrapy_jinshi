#!/usr/bin/python
# coding:utf-8

"""
Author: Andy Tian
Contact: tianjunning@126.com
Software: PyCharm
Filename: begin.py
Time: 2018/8/12 20:59
"""
import time
import os


n = 0
while True:
    print("第{}次爬取".format(n + 1))
    os.system('scrapy crawl js')
    time.sleep(60 * 3)
    n = n + 1

# from scrapy.cmdline import execute
# execute(['scrapy','crawl','js'])
