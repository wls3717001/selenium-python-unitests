# coding:utf-8
from selenium import webdriver  # 导入selenium
from selenium.webdriver.common.action_chains import ActionChains  # 悬停元素上方
from selenium.webdriver.support.select import Select  # select元素选择
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC  # 判断元素是否存在
driver = webdriver.Firefox()
url = "https://www.baidu.com"
driver.get(url)
mouse = WebDriverWait(driver, 10).until(lambda x: x.find_element("link text", "设置"))  # 使用显示等待方法判断元素存在后执行或者获取，10秒超时每隔0.5秒查询一次
ActionChains(driver).move_to_element(mouse).perform()
WebDriverWait(driver, 10).until(lambda x: x.find_element("link text", "搜索设置")).click()
#　选择设置项
s = WebDriverWait(driver, 10).until(lambda x: x.find_element("id", "nr"))
Select(s).select_by_visible_text("每页显示50条")
# 点保存按钮
js = 'document.getElementsByClassName("prefpanelgo")[0].click();'
driver.execute_script(js)
# 判断弹窗结果
result = EC.alert_is_present()(driver)
if result:
    print(result.text)
    result.accept()
else:
    print("alert 未弹出！")