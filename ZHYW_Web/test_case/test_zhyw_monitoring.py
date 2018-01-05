__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from custom_package import zhyw_login


class ZhywAutoY(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Ie()
        cls.driver.implicitly_wait(30)
        zhyw_login.Login().yw_login(cls.driver, "slt", "1")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_zhyw_system_auto1(self):
        u"""人员监控"""
        self.driver.find_element_by_xpath("//*[@id='10205']").click()
        self.driver.switch_to.frame("FrameRight")
        s = self.driver.find_element_by_id("ywdw")
        Select(s).select_by_value("100102010001")
        self.driver.find_element_by_id("repairerid").send_keys(u"郭志华")
        self.driver.find_element_by_id("btnselect").click()
        time.sleep(3)
        self.driver.switch_to.default_content()

    def test_zhyw_system_auto2(self):
        u"""工况数据"""
        above = self.driver.find_element_by_xpath("//div[@id='10209']")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("//*[@id='10209']/ul/li[1]/a").click()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_id("starttime").clear()
        self.driver.find_element_by_id("starttime").send_keys("2017-10-01")
        self.driver.find_element_by_id("endtime").clear()
        self.driver.find_element_by_id("endtime").send_keys("2017-10-01")
        self.driver.find_element_by_id("search").click()
        time.sleep(3)
        locator = ("xpath", "//*[@id='WkcdList']/tbody/tr[2]/td[2]")
        text = u"昌黎县兴国精密机件有限公司6号丼"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)
        self.driver.switch_to.default_content()

    def test_zhyw_system_auto3(self):
        u"""水情数据"""
        above = self.driver.find_element_by_xpath("//div[@id='10209']")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("//*[@id='10209']/ul/li[2]/a").click()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_id("starttime").clear()
        self.driver.find_element_by_id("starttime").send_keys("2017-08-07")
        self.driver.find_element_by_id("endtime").clear()
        self.driver.find_element_by_id("endtime").send_keys("2017-08-08")
        self.driver.find_element_by_id("search").click()
        time.sleep(3)
        locator = ("xpath", "//*[@id='WaterList']/tbody/tr[1]/td[2]")
        text = u"河北瑞禹塑料制品邮箱公司"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)
        self.driver.switch_to.default_content()

    def test_zhyw_system_auto4(self):
        u"""雨情数据"""
        above = self.driver.find_element_by_xpath("//div[@id='10209']")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("//*[@id='10209']/ul/li[3]/a").click()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_id("starttime").clear()
        self.driver.find_element_by_id("starttime").send_keys("2017-08-07")
        self.driver.find_element_by_id("endtime").clear()
        self.driver.find_element_by_id("endtime").send_keys("2017-08-08")
        self.driver.find_element_by_id("search").click()
        time.sleep(3)
        locator = ("xpath", "//*[@id='RainList']/tbody/tr[1]/td[2]")
        text = u"风帆股份有限公司有色金属公司2号井"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)
        self.driver.switch_to.default_content()

    def test_zhyw_system_auto5(self):
        u"""故障测站统计"""
        self.driver.find_element_by_xpath("//*[@id='10208']").click()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_class_name("btn-default").click()
        locator = ("xpath", "//*[@id='faultstationlist']/tbody/tr[1]/td[2]")
        text = u"河北省水文局"
        result = EC.text_to_be_present_in_element(locator, text)(self.driver)
        self.assertTrue(result)

    def test_zzz(self):
        self.driver.quit()










