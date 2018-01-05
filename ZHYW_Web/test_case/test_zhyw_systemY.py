__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from custom_package import zhyw_login
from selenium.webdriver.support.select import Select


class ZhywAutoY(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Ie()
        cls.driver.implicitly_wait(5)
        zhyw_login.Login().yw_login(cls.driver, "szy", "1")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_zhyw_system_auto1(self):
        u"""打开系统中心"""
        self.driver.find_element_by_xpath(".//*[@id='A106']").click()

    def test_zhyw_system_auto2(self):
        u"""测站管理页面"""
        above = self.driver.find_element_by_xpath("//div[@id='10604']")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("//div[@id='10604']/ul/li[1]/a").click()
        self.driver.switch_to.frame("FrameRight")
        s = self.driver.find_element_by_id("sttpCon")
        Select(s).select_by_value("QY")
        self.driver.find_element_by_id("search").click()
        self.driver.switch_to.default_content()

    def test_zhyw_system_auto3(self):
        u"""接收服务页面"""
        above = self.driver.find_element_by_xpath("//div[@id='10604']")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("//div[@id='10604']/ul/li[2]/a").click()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_css_selector("#addSur").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@class='aui_buttons']/button[2]").click()
        time.sleep(1)
        '''
        self.driver.find_element_by_class_name("combo-arrow").click()
        time.sleep(3)
        drop_down = self.driver.find_element_by_xpath("//div[@id='_easyui_combobox_i1_2']")
        ActionChains(self.driver).click(drop_down).click().perform()
        self.driver.find_element_by_xpath("//div[@class='user_sub']/button").click()
        '''

    def test_zhyw_system_auto4(self):
        u"""切换权限管理 公司管理"""
        above = self.driver.find_element_by_xpath("//div[@id='10602']")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("//div[@id='10602']/ul/li[1]/a").click()
        time.sleep(3)
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_id("editUnit").click()
        self.driver.find_element_by_css_selector(".ui-dialog-autofocus").click()
        self.driver.find_element_by_id("treeDemo_3_span").click()
        self.driver.find_element_by_xpath(".//*[@id='bootstraptable']/tbody/tr[1]/td[1]/input").click()
        self.driver.find_element_by_id("editUnit").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@class='aui_buttons']/button[2]").click()


    def test_zzz(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
