from pages.utilities import Utilities
import pytest

def test_login(username, password, setup_teardown):
    driver, login_page = setup_teardown

    expected_result = False
    if username == "locked_out_user":
        expected_result = True

    login_page.login(username, password)
    assert Utilities.has_error_message(driver) == expected_result

def test_logout(username, password, setup_teardown):
    driver, login_page = setup_teardown

    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")

    login_page.login(username, password)

    Utilities.open_menu(driver)
    Utilities.logout(driver)
    driver.back()

    assert driver.current_url == "https://www.saucedemo.com/"
    