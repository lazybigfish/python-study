import requests,json

#关于自动登陆评论的事情


session = requests.session()
#建立会话

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

#设置请求头

#读取本地cookies的函数
def reader_cookies():
    cookies_txt = open('cookies.txt', 'r')
    # reader读取模式，打开cookies文件
    cookies_dict = json.loads(cookies_txt.read())
    # 调用json模块的loads函数，把字符串转换成字典
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    # 把字典格式的cookies再转换成cookies原来的格式
    return (cookies)
    #返回cookies


#登陆的函数,并将cookies存入本地文件
def sigin():
    url = ''
    # 登陆的网址
    data = {

    }
    # 登陆的参数
    session.post(url, headers=headers, data=data)
    # session会话用post发起请求
    #下面代码是cookies调取存入本地
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    # 把cookies 专程成字典
    cookies_str = json.dumps(cookies_dict)
    # 调用json的dump函数，把cookies从字典再转换成字符串
    f = open('cookies.txt', 'w')
    # 创建本地cookies的文件，写入模式写入内容
    f.write(cookies_str)
    # 将cookies的字符串写进去
    f.close()

try:

    session.cookies = reader_cookies()
    #获取这个cookies

    # cookies_txt = open('cookies.txt','r')
    # #reader读取模式，打开cookies文件
    # cookies_dict = json.loads(cookies_txt.read())
    # #调用json模块的loads函数，把字符串转换成字典
    # cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    # #把字典格式的cookies再转换成cookies原来的格式
    # cookies = session.cookies
    # #获取cookies：调用requests对象（session）的cookies属性


except FileNotFoundError:
#如果try无法执行，将会报错文件找不到，然后执行下面的代码
    sigin()
    session.cookies = reader_cookies()

    # url = ''
    # #登陆的网址
    # data = {
    #
    # }
    # #登陆的参数
    # session.post(url,headers = headers,data = data)
    # #session会话用post发起请求

    # cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    # #把cookies 专程成字典
    # cookies_str = json.dumps(cookies_dict)
    # #调用json的dump函数，把cookies从字典再转换成字符串
    # f = open('cookies.txt','w')
    # #创建本地cookies的文件，写入模式写入内容
    # f.write(cookies_str)
    # #将cookies的字符串写进去
    # f.close()

#上方是登陆的代码块，下面是发表评论的代码块

url_1 = ''
#评论的网址
data_1 = {

}
#评论上传的参数
comment = session.post(url_1,headers = headers,data = data_1)
#在当前session会话下发起评论请求
print(comment.status_code)
#打印反馈状态