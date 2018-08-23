# -*- coding: utf-8 -*-
import time

import scrapy
import re
import redis

from scrapyProject.jinshi.jinshi.items import JinshiItem


class JsSpider(scrapy.Spider):
    name = 'js'
    allowed_domains = ['www.jin10.com']
    start_urls = ['http://www.jin10.com/']
    r = redis.Redis(host='localhost', port=6379)
    def parse(self, response):
        items = response.xpath('//div[@class="jin-flash_loading jin-flash_item"]')
        item = JinshiItem()
        for i in items:
            #time.sleep(1)
            link = i.xpath('.//a/@href').extract_first()
            data = re.search(r'(\d{14})', link.split('/')[-1]).group(1)
            msg = i.xpath('.//h4').extract_first().replace("<h4>", "").replace("</h4>", "").replace("<b>", '').replace("</b>", '')
            if not self.r.exists(data):
                self.r.set(data, data)
                item['link'] = link
                item['_id'] = data
                item['time'] = data[:4] + "/" + data[4:6] + "/" + data[6:8] + "  " + data[8:10] + ":" + data[10:12] + ":" + data[12:14]
                if msg:
                    item['msg'] = msg
                yield item
        #time.sleep(15)
        #yield scrapy.Request(url='http://www.jin10.com/',callback=self.parse)
