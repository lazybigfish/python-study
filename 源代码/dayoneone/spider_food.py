#爬取菜谱测试代码

import requests
from bs4 import BeautifulSoup

url = 'http://www.xiachufang.com/explore/'

res = requests.get(url)
html = res.text

soup = BeautifulSoup(html,'html.parser')

items = soup.find_all(class_='info pure-u')

list_food = []

for item in items:
    # tag_name = item.find('p',class_='name')
    # name = tag_name.text[17:-13]
    # tag_ellipsis = item.find('p',class_='ing ellipsis')
    # ellipsis = tag_ellipsis.text[1:-1]
    name = item.find('p', class_='name')
    ellipsis = item.find('p', class_='ing ellipsis')

    # list_food.append([name,ellipsis])

# print(list_food)
    print('菜名：',name.text[17:-13],'食材列表：',ellipsis.text[1:-1])

# print(items)
