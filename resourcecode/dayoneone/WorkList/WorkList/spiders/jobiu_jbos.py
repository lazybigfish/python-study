import bs4,scrapy

from ..items import WorklistItem


class WorkListSpider(scrapy.Spider):

    name = 'jobs'
    #命名爬虫名字

    allowed_domins = ['https://www.jobui.com']
    #允许爬去的网址范围

    start_urls = ['https://www.jobui.com/rank/company/']
    #初始爬的网址，从这里抓到后面要细抓的网址列表

    #抓取网址列表的函数
    def parse(self, response):

        bs = bs4.BeautifulSoup(response.text,'html.parser')

        ul_list = bs.find_all('ul',class_='textList flsty cfix')
        #这里找到招聘公司的网址列表

        for ul in ul_list:
            a_list = ul.find_all('a')
            #遍历这些包含网址数据

            for a in a_list:
                company_id = a['href']
                #取出包含的细节招聘的网址
                url = 'https://www.jobui.com{id}jobs'
                #构建初始的网址结构，留出位置填充后续补充进来的细节
                real_url = url.format(id = company_id)
                #生成最后的需要抓取的实际网址
                yield scrapy.Request(real_url,callback=self.parser_job)
                #scrapy.Request是构造requests对象的类。real_url是我们往requests对象里传入的每家公司招聘信息网址的参数。
                #callback的中文意思是回调。self.parser_job是我们新定义的parse_job方法。
                # 往requests对象里传入callback=self.parse_job这个参数后，引擎就能知道response要前往的下一站，是parse_job()方法。
                #yield语句就是用来把这个构造好的requests对象传递给引擎。


    #新的方法来抓取职位细节
    def parser_job(self,response):

        bs = bs4.BeautifulSoup(response.text,'html.parser')

        datas = bs.find_all('div', class_='job-simple-content-box')
        # 开始抓取职位列表

        company = bs.find(id = 'companyH1').text
        #公司名称的属性可以直接找出



        for data in datas:
            item = WorklistItem()
            # 实例化
            item['company'] = company

            item['position'] = data.find('div',class_='job-segmetation').find('a')['title']

            item['address'] = data.find('div', class_="job-desc").find('span')['title']

            item['detail'] = data.find('div', class_="job-desc").find_all('span')[1]['title']

            yield item
            # 用yield语句把item出去