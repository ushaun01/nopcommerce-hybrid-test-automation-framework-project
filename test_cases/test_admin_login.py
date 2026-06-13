import time

import pytest


from selenium import webdriver
from base_pages.login_admin_page import Login_Admin_Page
from utilities.custom_logger import Log_Maker
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config



class TestAdminLogin:
    admin_page_url = Read_Config.get_admin_page_url()                                #read values from read properties
    # read values from read properties
    username = Read_Config.get_username()
    password = Read_Config.get_password()                                  #we replaced hardcoded value by reading config from ini
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log()                                                 #call logger


    @pytest.mark.regression
#actual testcases
    def test_title_verification(self,setup):
        self.logger.info("*****Test 01 Title Verification*****")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        act_title = self.driver.title
        expected_title = 'nopCommerce demo store. Login'
        if act_title == expected_title:
            self.logger.info("*****Test 01 Title matched*****")
            assert True
        else:
            self.logger.info("*****Test 01 Title not matched*****")
            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    def test_valid_admin_login(self,setup):
        self.logger.info("*****Test 02 Valid Admin Login*****")
        self.driver = setup
        # options = webdriver.ChromeOptions()
        # # helps reduce automation detection
        # options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)
        # self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(15)
        dashboard_text = self.driver.find_element(By.XPATH,"//div[@class='content-header']/h1").text
        if dashboard_text == "Dashboard":
            self.logger.info("*****Test 01 valid login successfully*****")
            assert True

        else:
            self.logger.info("*****Test 01 valid login failed*****")
            self.driver.save_screenshot(".\\screenshots\\login_failure.png")
            assert False

    @pytest.mark.regression
    def test_invalid_admin_login(self,setup):
        self.logger.info("*****Test 03 Invalid Admin Login*****")
        # options = webdriver.ChromeOptions()
        # helps reduce automation detection
        # options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)
        # self.driver = webdriver.Chrome(options=options)
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)               #object of class Login_Admin_Page from base_pages
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(15)
        error_msg = self.driver.find_element(By.XPATH,"//li[normalize-space()='No customer account found']").text
        if error_msg == "No customer account found":
            self.logger.info("*****Test 03 invalid login error msg matched *****")
            assert True
            self.driver.save_screenshot(".\\screenshots\\invalid_login.png")

        else:
            self.logger.info("*****Test 03 invalid login failed*****")

            assert False
