__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC  # 判断元素条件
from selenium.webdriver.common.by import By
from custom_package import zhyw_login


class ZhywAutoY(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Ie()
        cls.driver.implicitly_wait(5)
        zhyw_login.Login().yw_login(cls.driver, 13030101, 1)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        pass


    def test_zhyw_system_auto1(self):
        u"""质量中心"""
        self.driver.find_element_by_xpath("//*[@id='A110']").click()
        locator = ("xpath", "//*[@id='11004']/a")
        text = u"运维质量评价"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)

    def test_zhyw_system_auto2(self):
        u"""质量中心查询"""
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_id("starttime").clear()
        self.driver.find_element_by_id("starttime").send_keys("2017-01-01")
        self.driver.find_element_by_id("starttime").send_keys(Keys.ESCAPE)
        self.driver.find_element_by_id("endtime").clear()
        self.driver.find_element_by_id("endtime").send_keys("2017-12-30")
        self.driver.find_element_by_id("endtime").send_keys(Keys.ESCAPE)
        k = self.driver.find_elements_by_class_name("btn-default")
        k[2].click()
        time.sleep(10)


    def test_zhyw_system_auto3(self):
        u"""打开数据列表"""
        # 完整率
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='commlist']/tbody/tr[1]/td[6]/div/a/span")))
        element.click()
        # self.driver.find_element_by_class_name("details").click()
        self.driver.switch_to.default_content()
        s = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//div[@class='aui_buttons']/button"))
        s.click()
        # 及时率
        self.driver.switch_to.frame("FrameRight")
        k = self.driver.find_elements_by_class_name("details")
        k[1].click()
        self.driver.switch_to.default_content()
        s = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//div[@class='aui_buttons']/button"))
        s.click()
        # 上传率
        self.driver.switch_to.frame("FrameRight")
        k = self.driver.find_elements_by_class_name("details")
        k[2].click()
        self.driver.switch_to.default_content()
        s = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//div[@class='aui_buttons']/button"))
        s.click()
        # 故障维修达标率
        self.driver.switch_to.frame("FrameRight")
        k = self.driver.find_elements_by_class_name("details")
        k[3].click()
        self.driver.switch_to.default_content()
        s = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//div[@class='aui_buttons']/button"))
        s.click()
        # 按时响应率
        self.driver.switch_to.frame("FrameRight")
        k = self.driver.find_elements_by_class_name("details")
        k[4].click()
        self.driver.switch_to.default_content()
        s = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//div[@class='aui_buttons']/button"))
        s.click()
        # 日均无故障时间
        self.driver.switch_to.frame("FrameRight")
        k = self.driver.find_elements_by_class_name("details")
        k[5].click()
        self.driver.switch_to.default_content()
        s = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//div[@class='aui_buttons']/button"))
        s.click()

    def test_zzz(self):
        self.driver.quit()





