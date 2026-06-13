from selenium.webdriver.common.by import By


class Login_Admin_Page:

#loactors:
    textbox_username_name = "Email"
    textbox_password_id = "Password"
    btn_login_xpath = "//button[@type='submit']"
    btn_logout_linktext = "Logout"


#constructor
    def __init__(self,driver):
        self.driver = driver

#action methods

    def enter_username(self,username):
        self.driver.find_element(By.NAME,self.textbox_username_name).clear()
        self.driver.find_element(By.ID,self.textbox_username_name).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.btn_logout_linktext).click()

