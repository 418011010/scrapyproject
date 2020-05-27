# -*- coding: utf-8 -*-
import scrapy
from scrapyproject.items import ScrapyprojectItem

class SegSpider(scrapy.Spider):
    name = 'seg'
    allowed_domains = ['www.segmentfault.com']
    start_urls = ['https://segmentfault.com/hottest/']

    def parse(self, response):
        divs = response.css('.news-list div')
        #divs = response.css('.col-md-7.middle h4,span,a')
        for d in divs:
            item1 = ScrapyprojectItem()
            item1['title'] = d.css('.mb5.mt5 h4::text').extract_first()
            item1['id'] = d.css('.news-item.stream__item.clearfix.mt15::attr(data-id)').extract_first()
            item1['votes'] = d.css('.news__item-meta span.votes-num  ::text').extract_first()
            item1['author'] = d.css('.news__item-meta a::text').extract_first()
            if item1['title'] and item1['id'] and item1['votes'] and item1['author']:
            
                yield(item1)
                print(len(item1))