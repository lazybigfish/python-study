import scrapy,bs4
from ..items import BookListItem
#x需要引用数据管道的函数来定义数据存放

class BookListSpider(scrapy.Spider):

    name = 'douban'
    #定义爬虫的名字叫dopuban

    allowed_domains = ['https://book.douban.com']
    #定义限制访问的网址范围，谨防跳出其他网站

    start_urls = []
    #定义一个空数组准备防止网址集合

    #通过for循环来填充网址进入网址集合
    for x in range(3):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)


    #通过parse函数来进行数据抓取和分析，该函数为scrapy自带
    def parse(self, response):
        #将自带函数抓取的数据response进行bs格式转换
        bs = bs4.BeautifulSoup(response.text,'html.parser')
        #找到该系列信息的要点进行抓取
        datas = bs.find_all('tr',class_='item')
        #通过for循环进行数据抓取和传送
        for data in datas:
            #定义一个对象，来自数据通道处理类
            item = BookListItem()
            #找到该数据的全部a的第二个的title属性，并填充进去item，下方几个类推
            item['title'] = data.find_all('a')[1]['title']

            item['original_title'] = data.find_all('span')[0].text

            item['publish'] = data.find('p',class_='pl').text

            item['score'] = data.find('span',class_='rating_nums').text

            print(item['title'])
            #将item通过yield传送出去
            yield item