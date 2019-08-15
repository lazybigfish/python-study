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
    url = 'http://www.weather.com.cn/weather/101240901.shtml'
    res = requests.get(url,headers = headers)
    #获取数据
    res.encoding = 'utf-8'

    # day = []
    # tem = []
    # wea = []
    # win = []
    seven_Day = []

    soup = BeautifulSoup(res.text,'html.parser')
    weatherDatas = soup.find('div', class_='c7d').find('ul').find_all('li')

    for weatherData in weatherDatas:
        day = weatherData.find('h1')
        tem = weatherData.find(class_='tem')
        # tem = tem.text
        # tem = tem[1:-1]
        wea = weatherData.find(class_='wea')
        seven_Day_data = [day.text,tem.text[1:-1],wea.text]
        seven_Day.append(seven_Day_data)


    # temple_data = weatherData.find(class_='tem')
    # weather_data = weatherData.find(class_='wea')

    # temple = temple_data.text
    # weather = weather_data.text
    #
    # return temple,weather
    weather_message = []
    for i in range(0,7):

        one = seven_Day[i][0] + '的温度：'+seven_Day[i][1]+'，气候为：'+seven_Day[i][2]
        weather_message.append(one)

    return weather_message

#发送数据到邮箱的函数
def send_email(seven_Day):


    global account,password,addressee

    mailhost = 'smtp.yeah.net'
    server = smtplib.SMTP()
    server.connect(mailhost,25)
    server.login(account,password)
    content = '最近的天气是：'+'\n'+seven_Day[0]+'\n'+seven_Day[1]+'\n'+seven_Day[2]+'\n'+seven_Day[3]+'\n'+seven_Day[4]+'\n'+seven_Day[5]+'\n'+seven_Day[6]
    message = MIMEText(content,'plain','utf-8')
    subject = '天气预报'
    message['Subject'] = Header(subject,'utf-8')
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