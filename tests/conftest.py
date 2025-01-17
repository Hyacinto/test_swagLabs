import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.login_page import Login
from pages.utilities import Utilities
import csv

def read_test_data():
    with open('data.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
        return [(row["username"], row["password"]) for row in data]

def pytest_generate_tests(metafunc):
    if "username" in metafunc.fixturenames and "password" in metafunc.fixturenames:
        test_data = read_test_data()
        metafunc.parametrize("username, password", test_data)

@pytest.fixture(scope="class")
def setup_teardown():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.saucedemo.com/")
    login_page = Login(driver)
    yield driver, login_page
    try:
        if driver.current_url != "https://www.saucedemo.com/" and "https://saucelabs.com/" not in driver.current_url :  
            Utilities.open_menu(driver)
            Utilities.reset(driver)
            Utilities.logout(driver)
    finally:
        driver.quit()