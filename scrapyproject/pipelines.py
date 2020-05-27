# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
import json
import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyprojectPipeline(object):
    def open_spider(self,spider):
        self.file = open('result.txt', 'w')
        print('file is opened')
    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False)+"\n")
        return item
    def close_spider(self,spider):
        self.file.close()
        print('file is closed')