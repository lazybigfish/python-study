import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    #将文件打开读取的内容存到redaer
    reader = csv.reader(f)
    #用来获取第一行的数据
    header_row = next(reader)
    #用来遍历表头的格式
    # for index,colum_header in enumerate(header_row):
    #     print(index,colum_header)
    dates,highs,lows = [],[],[]
    for row in reader:
        #提取时间，并且通过strptime函数转换格式
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        #遍历每行的第二个数据，并存储到highs
        high = int(row[1])
        highs.append(high)
        #遍历最低温出来
        low = int(row[2])
        lows.append(low)

    """绘制图形"""
    fig = plt.figure(dpi=128,figsize=(10,6))
    #设置数据来源，以及数据显示的颜色
    plt.plot(dates,highs,c='red')
    plt.plot(dates, lows, c='blue')
    #设置图片的格式
    plt.title("Daily high and low temperatures - 2014",fontsize = 24)
    plt.xlabel('high(red)-low(blue)',fontsize= 16)
    #使用标签倾斜
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)',fontsize = 16)
    plt.tick_params(axis='both',which='major',labelsize = 16)
    plt.show()
