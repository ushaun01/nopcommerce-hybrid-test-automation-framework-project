import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class SearchCustomer:
    #locators from search page
    text_email_id = "SearchEmail"
    text_firstname_id = "SearchFirstName"
    text_lastname_id = "SearchLastName"
    text_company_id = "SearchCompany"
    btn_search_id = "search-customers"

    rows_table_xpath = "//table[@id='customers-grid']/tbody//tr"
    columns_table_xpath = "//table[@id='customers-grid']/tbody//tr/td"

    def __init__(self, driver):
        self.driver = driver

    def enter_customer_email(self, email):
        self.driver.find_element(By.ID,self.text_email_id).clear()
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

    def enter_customer_firstname(self, firstname):
        self.driver.find_element(By.ID,self.text_firstname_id).clear()
        self.driver.find_element(By.ID,self.text_firstname_id).send_keys(firstname)

    def enter_customer_lastname(self, lastname):
        self.driver.find_element(By.ID,self.text_lastname_id).clear()
        self.driver.find_element(By.ID,self.text_lastname_id).send_keys(lastname)

    def enter_customer_company_id(self, company_id):
        self.driver.find_element(By.ID,self.text_company_id).clear()
        self.driver.find_element(By.ID,self.text_company_id).send_keys(company_id)

    def click_search_button(self):
        self.driver.find_element(By.ID,self.btn_search_id).click()

    def get_results_table_rows(self):
        return len(self.driver.find_elements(By.XPATH,self.rows_table_xpath))

    def get_results_table_columns(self):
        return len(self.driver.find_elements(By.XPATH,self.columns_table_xpath))

    def search_customer_by_email(self, email):
        email_present = False
        for r in range(1,self.get_results_table_rows()+1):
            cur_email = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td[2]").text

            if cur_email == email:
                email_present = True
                break
        return email_present

    def search_customer_by_name(self,name):
        name_present = False
        for r in range(1,self.get_results_table_rows()+1):
            cus_name = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td[3]").text
            if cus_name == name:
                name_present = True
                break
        return name_present

    def search_customer_by_company(self,company_name):
        company_present = False
        for r in range(1,self.get_results_table_rows()+1):
            cus_cum_name = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody//tr["+str(r)+"]/td[5]").text
            if cus_cum_name == company_name:
                company_present = True
                break
        return company_present