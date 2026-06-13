import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.login_admin_page import Login_Admin_Page
from base_pages.add_customer import AddCustomer
from base_pages.search_customer import SearchCustomer

class Test_Search_Customer:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log()

    @pytest.mark.regression
    def test_search_by_email(self,setup):
        self.logger.info("***Search Customer***")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(20)
        self.logger.info("***login success***")
        self.logger.info("***navigating to search page***")
        self.add_customer = AddCustomer(self.driver)
        self.add_customer.customer()
        self.add_customer.customer_menu()
        self.logger.info("***starting search customer by email***")
        self.search_customer = SearchCustomer(self.driver)
        self.search_customer.enter_customer_email("steve_gates@nopCommerce.com")
        self.search_customer.click_search_button()
        time.sleep(2)
        is_email = self.search_customer.search_customer_by_email("steve_gates@nopCommerce.com")
        if is_email == True:
            assert True
            self.logger.info("***search_customer_by_email***")
            self.driver.close()
        else:
            self.logger.info("***search_customer_by_email failed***")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_search_by_name(self,setup):
        self.logger.info("***Search Customer by name***")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)
        self.logger.info("***login success***")
        self.logger.info("***navigating to search page***")
        self.add_customer = AddCustomer(self.driver)
        self.add_customer.customer()
        self.add_customer.customer_menu()
        self.logger.info("***starting search customer by name***")
        self.search_customer = SearchCustomer(self.driver)
        self.search_customer.enter_customer_firstname("Steve")
        self.search_customer.enter_customer_lastname("Gates")
        self.search_customer.click_search_button()
        time.sleep(2)
        is_name = self.search_customer.search_customer_by_name("Steve Gates")
        if is_name == True:
            assert True
            self.logger.info("***search_customer_by_name***")
            self.driver.close()
        else:
            self.logger.info("***search_customer_by_name failed***")
            self.driver.close()
            assert False


    def test_search_by_companyname(self,setup):
        self.logger.info("***Search Customer by companyname***")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        time.sleep(10)
        self.logger.info("***login success***")
        self.logger.info("***navigating to search page***")
        self.add_customer = AddCustomer(self.driver)
        self.add_customer.customer()
        self.add_customer.customer_menu()
        self.logger.info("***starting search customer by companyname***")
        self.search_customer = SearchCustomer(self.driver)
        self.search_customer.enter_customer_company_id("Ratna")
        self.search_customer.click_search_button()
        time.sleep(2)
        is_companyname_present = self.search_customer.search_customer_by_company("Ratna")
        if is_companyname_present == True:
            assert True
            self.logger.info("***search_customer_by_companyname***")
            self.driver.close()
        else:
            self.logger.info("***search_customer_by_companyname failed***")
            self.driver.close()
            assert False



