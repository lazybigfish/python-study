import smtplib
# 导入发送邮件的的模块
from email.mime.text import MIMEText
#导入写邮件的函数MIMEText
from email.header import Header
#构建邮件头

from_addr = 'nbnqdcd@yeah.net'
#设置发信的邮箱账号
password = input('请输入授权码：')
#设置发信的账号授权码
to_addr = '840128511@qq.com'
#设置接受的邮箱
smtp_server = 'smtp.yeah.net'
#设置smtp服务器地址
msg = MIMEText('新的一邮件测试，但是这个没有debug，但是新增系统提示','plain','utf-8')
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('python test')
#设置邮件内容的格式

#开始发邮件

server = smtplib.SMTP()
#打开邮箱
server.connect(smtp_server,25)
# server.set_debuglevel(1)
server.login(from_addr,password)
#登陆邮箱
try:
    server.sendmail(from_addr, to_addr, msg.as_string())
    print('ok!')
except:
    print("发送失败！")
#发送邮件
server.quit()