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
        u"""设备中心 设备分类"""
        self.driver.find_element_by_xpath("//*[@id='A108']").click()
        above = self.driver.find_element_by_xpath("//div[@id='10803']")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("//*[@id='10803']/ul/li[1]/a").click()
        self.driver.switch_to.frame("FrameRight")
        s = self.driver.find_element_by_id("typeaid")
        Select(s).select_by_value("180000")
        self.driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/button").click()
        locator = ("xpath", "//*[@id='devicelist']/tbody/tr/td[4]")  # 验证那一行元素的定位方法
        text = u"水位计"  # 验证的文本
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)  # 判断元素内是否包含指定内容，返回布尔类型的值, Ture and False
        self.assertTrue(result)
        self.driver.switch_to.default_content()

    def test_zhyw_system_auto2(self):
        u"""设备型号"""
        self.driver.find_element_by_xpath("//*[@id='A108']").click()
        above = self.driver.find_element_by_xpath("//div[@id='10803']")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("//*[@id='10803']/ul/li[2]/a").click()
        self.driver.switch_to.frame("FrameRight")
        s = self.driver.find_element_by_id("typeaid")
        Select(s).select_by_value("110000")
        self.driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/button").click()
        locator = ("xpath", "//*[@id='productlist']/tbody/tr/td[5]")  # 验证那一行元素的定位方法
        text = u"数据采集仪（RTU）"  # 验证的文本
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)  # 判断元素内是否包含指定内容，返回布尔类型的值, Ture and False
        self.assertTrue(result)
        self.driver.find_element_by_id("saveParam").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@class='aui_buttons']/button[2]").click()

    def test_zhyw_system_auto3(self):
        u"""设备型号"""
        self.driver.find_element_by_xpath("//*[@id='A108']").click()
        above = self.driver.find_element_by_xpath("//div[@id='10803']")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("//*[@id='10803']/ul/li[3]/a").click()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_id("cmpnm").send_keys(u"艾力泰尔")
        self.driver.find_element_by_xpath("//div[@class='server_form']/div[5]/button").click()
        locator = ("xpath", "//*[@id='Manfulist']/tbody/tr/td[2]/a/span")  # 验证那一行元素的定位方法
        text = u"艾力泰尔"  # 验证的文本
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)  # 判断元素内是否包含指定内容，返回布尔类型的值, Ture and False
        self.assertTrue(result)
        self.driver.switch_to.default_content()

    def test_zzz(self):
        self.driver.quit()