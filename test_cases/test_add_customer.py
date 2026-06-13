import  string
import random
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.login_admin_page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.add_customer import AddCustomer

class Test_Add_New_Customer:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_new_customer(self,setup):
        self.logger.info("Test Add New Customer")
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(5)
        self.driver.maximize_window()
        self.logger.info("***********Login Successful*******")
        self.logger.info("**********Starting add new customer*******")
        self.add_customer = AddCustomer(self.driver)
        self.add_customer.customer()
        self.add_customer.customer_menu()
        self.add_customer.add_new()
        email = generate_random_email()
        self.add_customer.enter_email(email)
        self.add_customer.enter_password("Test@123")
        self.add_customer.enter_first_name("Usha")
        self.add_customer.enter_last_name("Shaw")
        self.add_customer.select_gender("Female")
        self.add_customer.enter_companyname("Ratna")
        self.add_customer.select_tax_exempt()
        self.add_customer.select_customer_role("Forum")
        self.add_customer.select_manager_of_vendor("Vendor 1")
        self.add_customer.enter_admincomment("Test admin comment")
        self.add_customer.click_save()
        time.sleep(5)

        #testcase validation
        customer_add_success = "The new customer has been added successfully."
        success_text = self.driver.find_element(By.XPATH,"//span[text()='The new customer has been added successfully.']").text
        if customer_add_success in success_text:
            assert True
            self.logger.info("Test Add New Customer Passed")
            self.driver.close()

        else:
            self.logger.info("Test Add New Customer Failed")
            self.driver.save_screenshot("D:\Today\nopcommerce-hybrid-framework\screenshots\test_add_new_customer.png")
            self.driver.close()
            assert False
















def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits))
    domain = random.choice(['gmail.com', 'example.com'])
    return  f'{username}@{domain}'

