# coding:utf-8
from selenium import webdriver

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

# 打开chrome浏览器
driver = webdriver.Chrome(chrome_options=option)
driver.get("https://www.cnblogs.com/yoyoketang")
print(driver.title)