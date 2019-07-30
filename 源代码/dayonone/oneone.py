import requests
from bs4 import BeautifulSoup


url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
res = requests.get(url)
#requests返回一个对象赋值给res

print('反馈状态：',res.status_code)

html = res.text
#res以字符串的形式返回给html

soup = BeautifulSoup(html,'html.parser')
#弟0哥属性必须为字符串,将网页解析为bs对象
items = soup.find_all(class_='books')

for item in items:
    kind = item.find('h2')
    title = item.find(class_='title')
    brief = item.find(class_='info')
    print(kind.text,'\n',title.text,'\n',title['href'],'\n',brief.text)
# print(type(soup))


# print(type(item))
# print(items)