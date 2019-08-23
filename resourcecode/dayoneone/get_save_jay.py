#通过selenium抓取数据

from selenium import  webdriver
from bs4 import BeautifulSoup
import time,openpyxl



#创建本地xlsx文件
wb = openpyxl.Workbook()
sheet = wb.active
#读取第一个工作簿并命名
sheet.title = 'one'
sheet['A1'] = '评论者'
sheet['B1'] = '评论内容'
sheet['C1'] = '评论时间'
sheet['D1'] = '赞'

# def get_conent():



url = 'https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

for i in range(0,4):

    button = driver.find_element_by_class_name('js_get_more_hot')
    button.click()
    time.sleep(1)


pageSource = driver.page_source
soup = BeautifulSoup(pageSource, 'html.parser')
items = soup.find(class_='js_hot_list').find_all(class_='js_cmt_li')
for item in items:
    name = item.find('h4')
    name = name.text
    content = item.find('p')
    content = content.text
    content_time = item.find('div').find('span')
    content_time = content_time.text
    zan = item.find(class_='js_cmt_praise').find('span')
    zan = zan.text

    sheet.append([name,content,content_time,zan])

wb.save('seven.xlsx')
# get_conent(driver)
driver.close()