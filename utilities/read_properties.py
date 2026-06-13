import configparser

config =configparser.RawConfigParser()            #object
config.read("D:/Today/nopcommerce-hybrid-framework/configurations/config.ini")                 #read config file and path of config

#fetch values by creating class
class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info', 'admin_page_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('admin login info', 'username')
        return username


    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password


    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('admin login info', 'invalid_username')
        return invalid_username

