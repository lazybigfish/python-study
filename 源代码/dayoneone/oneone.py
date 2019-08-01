import requests
from bs4 import BeautifulSoup

#爬出该网页所有评论。
# url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
url = 'https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/'
res = requests.get(url)
#requests返回一个对象赋值给res

print('反馈状态：',res.status_code)

html = res.text
#res以字符串的形式返回给html

soup = BeautifulSoup(html,'html.parser')
#弟0哥属性必须为字符串,将网页解析为bs对象
items = soup.find_all(class_='comment')

for item in items:
    time = item.find(class_='comment-metadata')
    author = item.find(class_='comment-author')
    conent = item.find(class_='comment-content')
    print(author.text,conent.text)

# print(type(soup))


# print(type(item))
# print(items)