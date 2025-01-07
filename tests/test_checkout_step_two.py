import pytest
from pages.inventory_page import Inventory
from pages.cart_page import Cart
from pages.checkout_step_one_page import Checkout_step_one
from pages.checkout_step_two_page import Checkout_step_two
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
        driver.quit()

def test_exit_checkout(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
    login_page.login(username, password)
    
    core_process(driver, username)

    checkout_step_two_page = Checkout_step_two(driver)
    checkout_step_two_page.back_to_products()
    
    expected_URL = "https://www.saucedemo.com/inventory.html"
    actual_URL = driver.current_url

    assert actual_URL == expected_URL

def test_checkout(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
    login_page.login(username, password)
    
    core_process(driver, username)

    checkout_step_two_page = Checkout_step_two(driver)
    checkout_step_two_page.checkout_finish()
    
    expected_URL = "https://www.saucedemo.com/checkout-complete.html"
    actual_URL = driver.current_url

    assert actual_URL == expected_URL

def test_do_the_math(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
    login_page.login(username, password)
    
    core_process(driver, username)    

    checkout_step_two_page = Checkout_step_two(driver)
    actual_result = checkout_step_two_page.total_price
    expected_result = checkout_step_two_page.calculate_total_price

    assert actual_result == expected_result

def test_compare_items(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
    login_page.login(username, password)
    
    inventory_page = Inventory(driver)
    inventory_page.basket_in_inventory()
    inventory_page.to_the_cart()
    
    cart_page = Cart(driver)
    titles_in_cart = cart_page.titles_cart
    descriptions_in_cart = cart_page.descriptions_cart
    prices_in_cart = cart_page.prices_cart
    cart_page.to_the_checkout()

    checkout_step_one_page = Checkout_step_one(driver)
    checkout_step_one_page.fill_the_fields("Elek", "Teszt", 5000)
    checkout_step_one_page.continue_checkout()
    
    if  Utilities.has_error_message(driver) == True:
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()

    checkout_step_two_page = Checkout_step_two(driver)
    
    assert(
        titles_in_cart == checkout_step_two_page.titles_checkout
        and descriptions_in_cart == checkout_step_two_page.descriptions_checkout
        and prices_in_cart == checkout_step_two_page.prices_checkout
    )