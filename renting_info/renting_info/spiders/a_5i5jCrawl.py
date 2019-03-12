# -*- coding: utf-8 -*-
import scrapy


class A5i5jcrawlSpider(scrapy.Spider):
    name = '_5i5jCrawl'
    allowed_domains = ['5i5j.com']
    start_urls = ['http://5i5j.com/']

    def parse(self, response):
        pass
