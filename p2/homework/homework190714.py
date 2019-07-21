# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By


class LoginDemo(unittest.TestCase):
    selenium_grid_url = "http://127.0.0.1:4444/wd/hub"
    capabilities = DesiredCapabilities.CHROME
    driver = webdriver.Remote(desired_capabilities=capabilities, command_executor=selenium_grid_url)
    driver.implicitly_wait(30)
    base_url = "http://www.doclever.cn"
    verificationErrors = []
    accept_next_alert = True

    def test_1_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url + "/controller/index/index.html")
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_css_selector("input.el-input__inner").clear()
        driver.find_element_by_css_selector("input.el-input__inner").send_keys("liwen629")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("Passw0rd")
        driver.find_element_by_id("login").click()
        time.sleep(5)
        self.assertTrue(self.is_element_present(By.ID,"tab-interface"))

    def test_2_creteAPI(self):
        # 代码忽略
        pass


    def test_3_logout(self):
        #代码忽略
        driver = self.driver
        driver.quit()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


if __name__ == "__main__":
    unittest.main()