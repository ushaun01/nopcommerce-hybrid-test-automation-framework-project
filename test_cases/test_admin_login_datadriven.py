
import time
import pytest
from selenium import webdriver
from base_pages.login_admin_page import Login_Admin_Page
from utilities.custom_logger import Log_Maker
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config
from utilities import excel_utilities



class TestAdminLogin_datadriven:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log()                                                 #call logger
    path = "D:/Today/nopcommerce-hybrid-framework/test_data/admin_login_data.xlsx"
    status_list = []
#actual testcase

    def test_valid_admin_login_datadriven(self,setup):
        self.logger.info("*****Test Valid Admin Login Data Driven Started*****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)

        self.rows = excel_utilities.getRowCount(self.path,'adim_login_data')
        print("number of row count",self.rows)






        for r in range(2,self.rows+1):
            self.username = excel_utilities.readData(self.path,'adim_login_data',r,1)
            self.password = excel_utilities.readData(self.path, 'adim_login_data', r, 2)
            self.expected_login = excel_utilities.readData(self.path, 'adim_login_data', r, 3)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()
            time.sleep(10)
            act_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if act_title == expected_title:
                if self.expected_login == "Yes":
                    self.logger.info("Test Data Driven Passed")
                    self.status_list.append("Passed")
                    self.admin_lp.click_logout()

                elif self.expected_login == "No":
                    self.logger.info("Test Data Driven Failed")
                    self.status_list.append("Failed")
                    self.admin_lp.click_logout()

            elif act_title != expected_title:
                if self.expected_login == "Yes":
                    self.logger.info("Test Data Driven Failed")
                    self.status_list.append("Failed")
                elif self.expected_login == "No":
                    self.logger.info("Test Data Driven Passed")
                    self.status_list.append("Passed")

        print("Status list is",self.status_list)
        if "Failed" in self.status_list:
            self.logger.info("Test Data Driven Failed")
            assert False
        else:
            self.logger.info("Test Data Driven Passed")
            assert True




