# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
class JinshiPipeline(object):
    def open_spider(self,spider):
        self.client = pymongo.MongoClient()
        self.db = self.client['jinshi']
        self.collection = self.db['jinshishuju']
    def process_item(self, item, spider):
            self.collection.save(dict(item))
            return item

    def close_spider(self,spider):
        self.client.close()
