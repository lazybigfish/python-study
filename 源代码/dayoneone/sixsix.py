#调用浏览器进行实例测试

#从selenium调用webdriver模块
from selenium import  webdriver
import time


#设置引擎为Chrome，打开一个浏览器
driver = webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)

teacher = driver.find_element_by_id('teacher')
#找到id为teacher的位置
teacher.send_keys('必须是吴枫呀')
#自动输入操作
assistant = driver.find_element_by_name('assistant')
assistant.send_keys('都喜欢')
time.sleep(1)
button = driver.find_element_by_class_name('sub')
time.sleep(1)
button.click()
driver.close()