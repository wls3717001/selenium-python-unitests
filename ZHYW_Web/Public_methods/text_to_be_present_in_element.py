# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
url = "https://www.baidu.com"
driver.get(url)

locator = ("name", "tj_trnews")  # 验证那一行元素的定位方法
text = u"糯米"  # 验证的文本
result = EC.text_to_be_present_in_element(locator, text)(driver)  # 判断元素内是否包含指定内容，返回布尔类型的值, Ture and False
result1 = EC.alert_is_present()(driver)  # 判断是否弹出警告框
print(type(result1))
if result:
    print(result1.text)
    result1.accept()
else:
    print("alert 未弹出！")

