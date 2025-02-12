import pytest
from pages.inventory_page import Inventory
from pages.cart_page import Cart
from pages.checkout_step_one_page import Checkout_step_one
from pages.checkout_step_two_page import Checkout_step_two
from pages.checkout_complete_page import Checkout_complete
from pages.utilities import Utilities

def core_process(driver, username):
    inventory_page = Inventory(driver)
    inventory_page.basket_in_inventory()
    inventory_page.to_the_cart()
    
    cart_page = Cart(driver)
    cart_page.to_the_checkout()
    
    checkout_step_one_page = Checkout_step_one(driver)
    checkout_step_one_page.fill_the_fields("Elek", "Teszt", 5000)
    checkout_step_one_page.continue_checkout()

    if  Utilities.has_error_message(driver) == True:
        pytest.fail(f"Test failed intentionally for user: {username}")

    checkout_step_two_page = Checkout_step_two(driver)
    checkout_step_two_page.checkout_finish()

def test_finished_checkout_and_back(username, password, setup_teardown):
    driver, login_page = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        
    login_page.login(username, password)
    
    core_process(driver, username)

    if driver.current_url != "https://www.saucedemo.com/checkout-complete.html":
        pytest.fail(f"Test failed intentionally for user: {username}")
        

    checkout_complete_page = Checkout_complete(driver)
    checkout_complete_page.back_to_products()
    
    expected_URL = "https://www.saucedemo.com/inventory.html"
    actual_URL = driver.current_url

    assert actual_URL == expected_URL

def test_finished_checkout(username, password, setup_teardown):
    driver, login_page = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        
    login_page.login(username, password)
    
    core_process(driver, username)
    
    expected_result = 0
    actual_result = Utilities.item_counter(driver)

    assert actual_result == expected_result
    
