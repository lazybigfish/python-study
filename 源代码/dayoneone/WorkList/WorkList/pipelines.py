# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import openpyxl
#导入opy模块

class WorklistPipeline(object):

    #初始化函数，当类实例化的时候，这方法就会启动
    def __init__(self):

        self.wb = openpyxl.Workbook()
        #创建一个工作簿
        self.ws = self.wb.active
        #定位建立活动表格
        self.ws.append(['公司','职位','地址','招聘细节'])
        #添加表头

    def process_item(self, item, spider):
    #这是默认处理item数据的函数
        line = [item['company'],item['position'],item['address'],item['detail']]
    #将数据以表格的形式赋值给line
        self.ws.append(line)
    #将line填充进表格
        return item


    def close_spider(self,spider):
        #爬虫结束是执行该函数
        self.wb.save('./WorkList.xlsx')
        #保存文件
        self.wb.close()
        #关闭！！！！！