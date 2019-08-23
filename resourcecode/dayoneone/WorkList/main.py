#该函数为主入口
# 数据抓取和分析在WorkList/spiders/jobui_jobs.py
#抓取的数据设置在WorkList/items.py
#数据存放为csv的设置在WorkList/settings.py的最末尾有解释
#数据存放为xlsx为WorkList/pipelines.py, 其中需要settings设置注释取消//ITEM_PIPELINES

from scrapy import cmdline

cmdline.execute(['scrapy','crawl','jobs'])
