import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddCustomer:
    customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    customer_menuoption_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    add_new_xpath = "//a[normalize-space()='Add new']"
    email_name = "Email"
    password_name = "Password"
    first_name_id = "FirstName"
    last_name_id = "LastName"
    gender_male_id = "Gender_Male"
    gender_female_id = "Gender_Female"
    company_name = "Company"
    tax_exempt_name = "IsTaxExempt"
    customer_role_xpath = "//input[@role='searchbox']"
    role_administrator_xpath = "//li[contains(text(),'Administrators')]"
    role_forum_xpath = "//li[contains(text(),'Forum Moderators')]"
    role_registered_xpath = "//li[contains(text(),'Registered')]"
    role_guests_xpath = "//li[contains(text(),'Guests')]"
    role_vendors_xpath = "//li[contains(text(),'Vendors')]"
    managerofvendor_id = "VendorId"
    admincomment_name = "AdminComment"
    save_name = "save"

    def __init__(self, driver):
        self.driver = driver

    def customer(self):
        self.driver.find_element(By.XPATH,self.customer_menu_xpath).click()

    def customer_menu(self):
        self.driver.find_element(By.XPATH,self.customer_menuoption_xpath).click()

    def add_new(self):
        self.driver.find_element(By.XPATH,self.add_new_xpath).click()

    def enter_email(self,email):
        self.driver.find_element(By.NAME,self.email_name).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.NAME,self.password_name).send_keys(password)

    def enter_first_name(self,firstname):
        self.driver.find_element(By.ID,self.first_name_id).send_keys(firstname)

    def enter_last_name(self,lastname):
        self.driver.find_element(By.ID,self.last_name_id).send_keys(lastname)

    def select_gender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.gender_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID,self.gender_female_id).click()
        else:
            self.driver.find_element(By.ID,self.gender_female_id).click()

    def enter_companyname(self,companyname):
        self.driver.find_element(By.NAME,self.company_name).send_keys(companyname)

    def select_tax_exempt(self):
        self.driver.find_element(By.NAME,self.tax_exempt_name).click()

    def select_customer_role(self,role):
        elements=self.driver.find_elements(By.XPATH,self.customer_role_xpath)
        customer_field = elements[0]
        customer_field.click()
        time.sleep(5)
        if role == "Guests":
            self.driver.find_element(By.XPATH,self.role_guests_xpath).click()
            time.sleep(5)
            customer_field.click()
            self.driver.find_element(By.XPATH,self.role_forum_xpath).click()

        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH,self.role_forum_xpath).click()
        elif role == "Administrators":
            self.driver.find_element(By.XPATH,self.role_administrator_xpath).click()
        elif role == "Forum":
            self.driver.find_element(By.XPATH,self.role_forum_xpath).click()
        elif role == "Vendors":
            self.driver.find_element(By.XPATH,self.role_vendors_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.role_registered_xpath).click()

    def select_manager_of_vendor(self, value):
        element = self.driver.find_element(By.ID, self.managerofvendor_id)
        drp_down = Select(element)
        drp_down.select_by_visible_text(value)

    def enter_admincomment(self,admincomment):
        self.driver.find_element(By.NAME,self.admincomment_name).send_keys(admincomment)

    def click_save(self):
        self.driver.find_element(By.NAME,self.save_name).click()