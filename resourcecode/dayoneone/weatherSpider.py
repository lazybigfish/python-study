import requests,time,smtplib,schedule

from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header


account = input('输入你的邮箱：')
password = input('输入你的授权码：')
addressee = input('输入收件邮箱：')



#抓取数据的函数并分析出结果
def weather_spider():
    headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    #构建浏览器伪装标示
    url = 'http://www.weather.com.cn/weather/101240901.shtml'
    #输入抓取的网址
    res = requests.get(url,headers = headers)
    #获取数据
    res.encoding = 'utf-8'
    #因为编码问题，重新编码

    seven_Day = []
    #新建一个数据存放抓取出来的初始数据值

    soup = BeautifulSoup(res.text,'html.parser')
    #转换为bs对象
    weatherDatas = soup.find('div', class_='c7d').find('ul').find_all('li')
    #通过find方法，逐层找到关键信息

    #通过遍历将细节信息存放至seven_day
    for weatherData in weatherDatas:
        day = weatherData.find('h1')
        tem = weatherData.find(class_='tem')
        # tem = tem.text
        # tem = tem[1:-1]
        wea = weatherData.find(class_='wea')
        seven_Day_data = [day.text,tem.text[1:-1],wea.text]
        seven_Day.append(seven_Day_data)

    #生成正式的七天天气信息数组
    weather_message = []
    for i in range(0,7):

        one = seven_Day[i][0] + '的温度：'+seven_Day[i][1]+'，气候为：'+seven_Day[i][2]
        weather_message.append(one)

    return weather_message

#发送数据到邮箱的函数
def send_email(seven_Day):


    global account,password,addressee
    #全局化三个参数

    mailhost = 'smtp.yeah.net'
    #设置邮箱host
    server = smtplib.SMTP()
    #新启一个邮箱服务
    server.connect(mailhost,25)
    #通过服务连接邮箱
    server.login(account,password)
    #通过服务登陆邮箱
    content = '最近的天气是：'+'\n'+seven_Day[0]+'\n'+seven_Day[1]+'\n'+seven_Day[2]+'\n'+seven_Day[3]+'\n'+seven_Day[4]+'\n'+seven_Day[5]+'\n'+seven_Day[6]
    #设置需要发送的文本信息模板
    message = MIMEText(content,'plain','utf-8')
    #设置需要发送的文本信息
    subject = '天气预报'
    #设置邮件标题
    message['Subject'] = Header(subject,'utf-8')
    message['From'] = Header(account)
    message['To'] = Header(addressee)

    server.set_debuglevel(1)
    try:
        server.sendmail(account,addressee,message.as_string())
        print('发送成功!')
    except:
        print('errow!')


    server.quit()

#执行总函数
def job():
    print('开始任务！')
    weather_message = weather_spider()
    send_email(weather_message)
    print('完成任务！')


job()
#定时设置
# schedule.every().day.at("08:30").do(job)
# schedule.every(10).seconds.do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(2)