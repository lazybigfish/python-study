# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookListItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()
    #定义中文书名的数据属性
    original_title = scrapy.Field()
    #定义原名
    publish = scrapy.Field()
    #定义出版社信息的数据属性
    score = scrapy.Field()
    #定义评分的书数据属性
