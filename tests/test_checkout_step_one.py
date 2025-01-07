import pytest
from pages.inventory_page import Inventory
from pages.cart_page import Cart
from pages.checkout_step_one_page import Checkout_step_one
from pages.utilities import Utilities

checkout_data = [
        ("Elek", "Teszt", "5000"),
        ("", "Teszt", "5000"),
        ("Elek", "", "5000"),
        ("Elek", "Teszt", ""),
        ("", "", "")
    ]

def core_process(driver):
    inventory_page = Inventory(driver)
    inventory_page.basket_in_inventory()
    inventory_page.to_the_cart()
    
    cart_page = Cart(driver)
    cart_page.to_the_checkout()

@pytest.mark.parametrize("first_name, last_name, postal_code", checkout_data)
def test_fill_the_fields(username, setup_teardown, first_name, last_name, postal_code):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
    login_page.login(username, password)

    core_process(driver)

    checkout_step_one_page = Checkout_step_one(driver)
    checkout_step_one_page.fill_the_fields(first_name, last_name, postal_code)
    checkout_step_one_page.continue_checkout()
    
    if first_name == "" or last_name == "" or postal_code == "" or username == "problem_user":
        assert Utilities.has_error_message(driver)
    else:
        assert not Utilities.has_error_message(driver)

def test_cancel_checkout(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
    login_page.login(username, password)

    core_process(driver)

    checkout_step_one_page = Checkout_step_one(driver)
    checkout_step_one_page.cancel_checkout()
    
    expected_URL = "https://www.saucedemo.com/cart.html"
    actual_URL = driver.current_url

    assert actual_URL == expected_URL

def test_fields_show_the_text(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
    login_page.login(username, password)

    core_process(driver)

    checkout_step_one_page = Checkout_step_one(driver)
    checkout_step_one_page.fill_the_fields("Elek", "Teszt", "5000")
    first_name, last_name, postal_code = checkout_step_one_page.get_all_fields()
    
    assert first_name == "Elek"
    assert last_name == "Teszt"
    assert postal_code == "5000"
    
   

