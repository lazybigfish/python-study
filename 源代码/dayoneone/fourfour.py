#抓取的数据存取本地


import csv

import openpyxl

#第一种方法
# file = open('test.csv','a+')
#
# file.write('ddddd,dddd,ssss')
#
# file.close()
#第二中
# csv_file = open('demon.csv','w',newline='',encoding='utf-8')
#
# writer = csv.writer(csv_file)
#
# writer.writerow(['dddd','ssss'])
#
# csv_file.close()

#第三种

# wb = openpyxl.workbook()
# #创建新的workbook工作噗
# sheet = wb.active
# #获取该工作簿 的第一个工作表
# sheet.title = 'new title'
# #命名该工作表
# sheet['A1'] = '漫威'
# row = ['美国队长','蜘蛛侠','钢铁侠']
# sheet.append(row)
# wb.save('mavr.xlsx')


wb=openpyxl.Workbook()
#注意大写
sheet=wb.active
sheet.title='new title'
sheet['A1'] = '漫威宇宙'
rows= [['美国队长','钢铁侠','蜘蛛侠'],['是','漫威','宇宙', '经典','人物']]
for i in rows:
    sheet.append(i)
print(rows)
wb.save('Marvel.xlsx')
