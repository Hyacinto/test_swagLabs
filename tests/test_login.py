import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.login_page import Login
from pages.utilities import Utilities

# Helper function to extract user data only
def get_user_data():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.saucedemo.com/")
    login_page = Login(driver)
    usernames = login_page.get_usernames()  # Fetch usernames
    password = login_page.get_password()   # Fetch password
    driver.quit()  # Close browser after data extraction
    return usernames, password

# Dynamic parameterization without redundant driver initialization
def pytest_generate_tests(metafunc):
    if "username" in metafunc.fixturenames:
        usernames, _ = get_user_data()  # Only extract usernames
        metafunc.parametrize("username", usernames)

# Fixture to handle setup and teardown for Selenium
@pytest.fixture(scope="class")
def setup_teardown():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.saucedemo.com/")
    login_page = Login(driver)
    usernames, password = get_user_data()  # Reuse helper function for consistency

    yield driver, login_page, usernames, password

    driver.quit()

# Test function
def test_login(username, setup_teardown):
    driver, login_page, _, password = setup_teardown

    expected_result = False
    if username == "locked_out_user":
        expected_result = True

    # Perform login
    login_page.login(username, password)
    assert login_page.has_error_message() == expected_result

    # Logout after a successful login
    if driver.current_url == "https://www.saucedemo.com/inventory.html":
        Utilities.logout(driver)
