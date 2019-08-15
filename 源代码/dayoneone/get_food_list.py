import requests,bs4,csv,gevent
from gevent.queue import Queue
from bs4 import BeautifulSoup
from gevent import monkey
monkey.patch_all()

#导入所需第三方库，并将程序转换为异步模式

work = Queue()
#建立一个空的队列

url_1 = 'http://www.boohee.com/food/group/{type}?page={page}'
#url的模板原型
#for循环1-4填充到网页url
for x in range(1,4):
    for y in range(1,4):
        real_url = url_1.format(type = x,page = y)
        work.put_nowait(real_url)
        #将生成的网址填入work队列



def crawler():
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    #开始先验证队列是否为空
    while not work.empty():
        url = work.get_nowait()
        #爬虫所需的网址从work队列中获取
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        heat_list = soup.find_all('li', class_='item clearfix')
        for heat in heat_list:
            food_name = heat.find('div', class_='text-box').find('h4').text
            food_heat = heat.find('div', class_='text-box').find('p').text
            print(food_name,food_heat)


tasks_list = []
#建立一个任务数组
#通过for循环添加五个爬虫任务进入任务数组
for x in range(5):
    task = gevent.spawn(crawler)
    #通过spawn函数建立爬虫任务
    tasks_list.append(task)
    #将爬虫任务加入数组

gevent.joinall(tasks_list)
#执行任务数组的全部任务