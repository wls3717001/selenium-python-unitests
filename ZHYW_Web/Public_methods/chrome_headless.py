__author__ = 'Administrator'
# coding:utf-8
from selenium import webdriver

option = webdriver.ChromeOptions() # 静默模式
option.add_argument('headless')  # 静默模式
# 打开chrome浏览器
driver = webdriver.Chrome( chrome_options=option)
driver.get("https://www.baidu.com")
print(driver.title)