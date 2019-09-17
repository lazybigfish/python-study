import requests
import json
import pygal

# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# req = requests.get(json_url)
# with open('btc_close_2017_request.json','w') as f:
#     f.write(req.text)
# file_requests = req.json()

filename = 'btc_close_2017.json'
#打开json文件，并将数据读取存入btc_data
with open(filename) as f:
    btc_data = json.load(f)
#开始存放绘制的数据存放的表
dates = []
months = []
weeks = []
weekdays = []
close = []
#遍历数据，取出数值
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    #对数值进行整数化
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    #因为小数点无法直接整数，先转换浮点，在转换整数
    close.append(int(float(btc_dict['close'])))
    # print("{} is month {} week {} ,{},the close price is {} RMB".format(date,month,week,weekday,close))
    line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
    line_chart.title = '收盘价'
    line_chart.x_labels = dates
    N = 20  #x轴20天显示一次
    line_chart._x_labels_major = dates[::N]
    line_chart.add('收盘价',close)
    line_chart.render_to_file('收盘价图.svg')
