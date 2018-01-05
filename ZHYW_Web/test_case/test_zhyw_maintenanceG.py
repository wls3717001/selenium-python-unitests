__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import datetime
from selenium.webdriver.support import expected_conditions as EC
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
        u""" 切换到维护中心 """
        self.driver.find_element_by_xpath("//*[@id='A103']").click()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_id("addRequest").click()
        self.driver.switch_to.default_content()
        iframe = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_id("requester").send_keys("test1")
        self.driver.find_element_by_id("rmobile").send_keys("15246895236")
        self.driver.find_element_by_id("titleid").send_keys("测试002")
        self.driver.find_element_by_xpath("//*[@id='source']/div[1]/input").click()
        self.driver.find_element_by_id("contents").send_keys(u"测站故障，急需维修")
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//*[@class='aui_buttons']/button[1]").click()

    def test_zhyw_system_auto2(self):
        u""" 事件管理 """
        self.driver.find_element_by_xpath("//*[@id='10302']/a").click()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_xpath("//*[@id='eventList']/tbody/tr/td[8]/a[1]").click()
        self.driver.switch_to.default_content()
        time.sleep(2)
        iframe = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(iframe)
        s = self.driver.find_element_by_id("levelid")
        Select(s).select_by_value("2")
        self.driver.find_element_by_id("id1").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@class='aui_buttons']/button[2]").click()
        iframe = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath("//*[@id='sendlist']/tbody/tr/td[1]/input").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_class_name("aui_state_highlight").click()
        time.sleep(2)
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_xpath("//*[@id='bd']/div[7]/div/table/tbody/tr[3]/td/div[2]/button").click()
        self.driver.switch_to.default_content()

    def test_zhyw_system_auto3(self):
        u""" 巡检管理 """
        t = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 获取当前时间
        today = datetime.date.today()  # 获取当前时间
        laterday = today + datetime.timedelta(days=10)  # 获取10天后时间
        self.driver.find_element_by_xpath("//*[@id='10304']/a").click()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_xpath("//div[@id='addEvent']/span").click()
        self.driver.switch_to.default_content()
        iframe = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_id("title").send_keys(u"测试巡检test" + str(today))
        self.driver.find_element_by_id("startdate").send_keys(str(today))
        self.driver.find_element_by_id("enddate").send_keys(str(laterday))
        s = self.driver.find_element_by_id("select1")
        Select(s).select_by_value("100102010001")
        self.driver.find_element_by_id("rightMove").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_class_name("aui_state_highlight").click()
        self.driver.switch_to.alert.accept()
        time.sleep(3)

    def test_zhyw_system_auto4(self):
        u""" 测站数据审核 """
        self.driver.find_element_by_xpath("//*[@id='10306']/a").click()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_id("starttime").send_keys("2017-08-17")
        self.driver.find_element_by_id("endtime").send_keys("2017-12-30")
        s = self.driver.find_elements_by_class_name("btn-default")
        s[0].click()

    def test_zzz(self):
        self.driver.quit()












