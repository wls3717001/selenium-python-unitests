__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC  # 判断元素条件
from selenium.webdriver.common.by import By
from custom_package import zhyw_login


class ZhywAutoY(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Ie()
        cls.driver.implicitly_wait(5)
        zhyw_login.Login().yw_login(cls.driver, "13030101", "1")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_zhyw_system_auto1(self):
        u"""打开系统中心"""
        self.driver.find_element_by_xpath(".//*[@id='A106']").click()

    def test_zhyw_system_auto2(self):
        u"""切换人员管理"""
        above = self.driver.find_element_by_xpath("//div[@id='10602']")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("//div[@id='10602']/ul/li[2]/a").click()
        time.sleep(3)
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_xpath("//*[@id='addUser']").click()
        self.driver.switch_to.default_content()

    def test_zhyw_system_auto3(self):
        u"""添加人员"""
        new_time = time.strftime('%S', time.localtime())
        iframe = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_id("usercard").send_keys("jyb" + new_time)
        self.driver.find_element_by_id("userpwd").send_keys("1")
        self.driver.find_element_by_id("username").send_keys("甲乙丙" + new_time)
        time.sleep(1)
        s = self.driver.find_element_by_id("roleid")
        Select(s).select_by_value("36")
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@class='aui_buttons']/button[1]").click()
        time.sleep(3)

    def test_zhyw_system_auto4(self):
        u"""菜单管理"""
        above = self.driver.find_element_by_xpath("//div[@id='10602']")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("//div[@id='10602']/ul/li[3]/a").click()
        self.driver.switch_to.frame("FrameRight")
        s = self.driver.find_elements_by_class_name("combo-arrow")
        s[0].click()
        time.sleep(3)
        drop_down1 = self.driver.find_element_by_xpath("//div[@id='_easyui_combobox_i3_2']")
        ActionChains(self.driver).click(drop_down1).click().perform()
        s[1].click()
        time.sleep(3)
        drop_down2 = self.driver.find_element_by_xpath("//div[@id='_easyui_combobox_i4_2']")
        ActionChains(self.driver).click(drop_down2).click().perform()
        self.driver.find_element_by_xpath("//div[@class='user_sub']/button").click()
        self.driver.switch_to.default_content()

    def test_zhyw_system_auto5(self):
        u"""人员权限"""
        above = self.driver.find_element_by_xpath("//div[@id='10602']")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("//div[@id='10602']/ul/li[4]/a").click()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_id("treeDemo_29_span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='station_ab']").click()
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@class='aui_buttons']/button[2]").click()

    def test_zhyw_system_auto6(self):
        u"""角色管理"""
        above1 = self.driver.find_element_by_xpath("//div[@id='10602']")
        ActionChains(self.driver).move_to_element(above1).perform()
        self.driver.find_element_by_xpath("//div[@id='10602']/ul/li[5]/a").click()
        above2 = self.driver.find_element_by_xpath("//*[@id='thrMenu']")
        ActionChains(self.driver).move_to_element(above2).perform()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_id("addRole").click()
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector(".aui_buttons>button").click()
        # self.driver.find_element_by_xpath("//div[@class='aui_buttons']/button[2]").click()

    def test_zzz(self):
        self.driver.quit()


