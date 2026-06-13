import pytest
from selenium import webdriver

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()


#  helps reduce automation detection
@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

#hooks for adding environment info in html report
from pytest_metadata.plugin import metadata_key

def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'Ecommerce Project, Nopcommerce'
    config.stash[metadata_key] ['Tester Name'] = 'Usha'

#hooks for delete environment info in html report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('Plugins', None)




