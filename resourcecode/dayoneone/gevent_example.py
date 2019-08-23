from gevent import monkey
#导入monkey模块
monkey.patch_all()
#将程序异步处理

import gevent,time,requests

from gevent.queue import Queue
#导入queue模块

start = time.time()
#开始计时

url_list = ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']

work = Queue()
#创建队列对象，并赋值给work

#遍历URL数组
for url in url_list:
    work.put_nowait(url)
    #用put函数将遍历出来的网址都放进work队列

def crawler():
    while not work.empty():
        #当检查队列不为空当时候开始以下操作
        url = work.get_nowait()
        #将url从队列中获取
        r = requests.get(url)
        #抓取数据
        print(url,work.qsize(),r.status_code)
        #打印url，队列剩余值，反馈状态


tasks_list = []
#新建一个数组，存放爬虫任务

for x in range(2):
    task = gevent.spawn(crawler)
    #用spawn函数创建执行爬虫当任务
    tasks_list.append(task)
    #将创建当爬虫任务放进任务数组


gevent.joinall(tasks_list)
#执行任务数组里当所有任务，相当于同时启动两个爬虫
end = time.time()
print(end - start)