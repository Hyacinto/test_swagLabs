import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.login_page import Login
from pages.utilities import Utilities

# Helper function to initialization of Selenium and the data extraction
def init_browser_and_get_data():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.saucedemo.com/")
    login_page = Login(driver)
    usernames = login_page.usernames
    password = login_page.password
    return driver, login_page, usernames, password

@pytest.fixture(scope="class")
def setup_teardown():
    driver, login_page, usernames, password = init_browser_and_get_data()

    yield driver, login_page, usernames, password

    driver.quit()

# Dynamic parametering
def pytest_generate_tests(metafunc):
    if "username" in metafunc.fixturenames:
        _, _, usernames, _ = init_browser_and_get_data()
        metafunc.parametrize("username", usernames)

# Test function
def test_login(username, setup_teardown):
    driver, login_page, usernames, password = setup_teardown

    expected_result = False
    if username == "locked_out_user":
        expected_result = True

    # Login
    login_page.login(username, password)
    assert login_page.error_message() == expected_result

    # Logout, after a successful login
    if driver.current_url == "https://www.saucedemo.com/inventory.html":
        Utilities.logout(driver)

