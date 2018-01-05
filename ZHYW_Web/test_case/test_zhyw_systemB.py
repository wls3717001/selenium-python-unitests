# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from custom_package import zhyw_login



class ZhywAutoB(unittest.TestCase):
    '''
    dr = webdriver.Chrome()

    def setUp(self, driver=dr):
        self.driver = driver
        self.driver.implicitly_wait(30)
    '''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Ie()
        cls.driver.implicitly_wait(5)
        zhyw_login.Login().yw_login(cls.driver, "13030101", "1")
        cls.driver.maximize_window()

    def isElementExist(self, element):
        flag = True
        browser = self.driver
        try:
            browser.find_element_by_xpath(element)
            return flag
        except:
            flag = False
            return flag

    def test_zhyw_system_auto1(self):
        u""" 打开系统中心 """
        self.driver.find_element_by_xpath(".//*[@id='A106']").click()
        self.driver.get_screenshot_as_file("E:\\test_object\\screenshot\\system_center.png")

    def test_zhyw_system_auto2(self):
        u""" 切换合同页面 """
        above = self.driver.find_element_by_xpath("//div[@id='10603']")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("//div[@id='10603']/ul/li/a").click()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_id("addContract").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[3]").click()
        time.sleep(2)


    def test_zhyw_system_auto3(self):
        u""" 切换合SLA面 """
        above = self.driver.find_element_by_xpath("//div[@id='10603']")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_xpath("//div[@id='10603']/ul/li[2]/a").click()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_id("addSla").click()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]").click()
        time.sleep(2)

    def test_zhyw_system_auto4(self):
        u""" 切换合字典页面 """
        above = self.driver.find_element_by_xpath("//div[@id='10603']")
        ActionChains(self.driver).move_to_element(above).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@id='10603']/ul/li[3]/a").click()
        self.driver.switch_to.frame("FrameRight")
        self.driver.find_element_by_id("addDic").click()
        time.sleep(2)
        self.driver.get_screenshot_as_file("E:\\test_object\\screenshot\\dictionary.png")
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]").click()
        time.sleep(3)

    def test_zhyw_system_auto5(self):
        u""" 字典页面条件查询 """
        driver = self.driver
        driver.switch_to.frame("FrameRight")
        m = driver.find_elements_by_class_name("combo-arrow")
        m[0].click()
        time.sleep(3)
        js1 = 'document.getElementsByClassName("combo-panel")[0].scrollTop=10000'
        driver.execute_script(js1)
        drop_down1 = self.driver.find_element_by_xpath("//*[@id='_easyui_combobox_i1_81']")
        ActionChains(self.driver).click(drop_down1).click().perform()
        m[1].click()
        js2 = 'document.getElementsByClassName("combo-panel")[1].scrollTop=10000'
        driver.execute_script(js2)
        drop_down2 = self.driver.find_element_by_xpath("//*[@id='_easyui_combobox_i2_1']")
        ActionChains(self.driver).click(drop_down2).click().perform()
        self.driver.find_element_by_xpath("//div[@class='user_sub']/button").click()
        driver.switch_to.default_content()

    def test_zzz(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        print(time.strftime("%H:%M:%S"))