# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WorklistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    company = scrapy.Field()
    #公司存放的属性
    position = scrapy.Field()
    #职位存放的属性
    address = scrapy.Field()
    #工作地点
    detail = scrapy.Field()
    #职位细节描述
