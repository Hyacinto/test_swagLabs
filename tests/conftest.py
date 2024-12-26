import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.login_page import Login
from pages.utilities import Utilities

@pytest.fixture(scope="class")
def setup_teardown():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.saucedemo.com/")
    login_page = Login(driver)
    usernames = login_page.get_usernames()
    password = login_page.get_password()

    yield driver, login_page, usernames, password

    if driver.current_url != "https://www.saucedemo.com/":   
        Utilities.open_menu(driver)
        Utilities.reset(driver)
        Utilities.logout(driver)
        
    driver.quit()

def pytest_generate_tests(metafunc):
    if "username" in metafunc.fixturenames:
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("https://www.saucedemo.com/")
        login_page = Login(driver)
        usernames = login_page.get_usernames()
        driver.quit()
        metafunc.parametrize("username", usernames)