import pytest
from pages.inventory_page import Inventory
from pages.cart_page import Cart
from pages.checkout_step_one_page import Checkout_step_one
from pages.checkout_step_two_page import Checkout_step_two

def core_process(driver):
    inventory_page = Inventory(driver)
    inventory_page.basket_in_inventory()
    inventory_page.to_the_cart()
    
    cart_page = Cart(driver)
    cart_page.to_the_checkout()
    
    checkout_step_one_page = Checkout_step_one(driver)
    checkout_step_one_page.fill_the_fields("Elek", "Teszt", 5000)
    checkout_step_one_page.continue_checkout()

def test_exit_checkout(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
    login_page.login(username, password)
    
    core_process(driver)

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
    
    core_process(driver)

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
    
    core_process(driver)    

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
    titles_in_cart = cart_page.title_cart
    descriptions_in_cart = cart_page.description_cart
    prices_in_cart = cart_page.price_cart
    cart_page.to_the_checkout()

    checkout_step_one_page = Checkout_step_one(driver)
    checkout_step_one_page.fill_the_fields("Elek", "Teszt", 5000)
    checkout_step_one_page.continue_checkout()

    checkout_step_two_page = Checkout_step_two(driver)
    titles_in_checkout = checkout_step_two_page.title_checkout
    descriptions_in_checkout = checkout_step_two_page.description_checkout
    prices_in_checkout = checkout_step_two_page.price_checkout

    assert(
        titles_in_cart == titles_in_checkout
        and descriptions_in_cart == descriptions_in_checkout
        and prices_in_cart == prices_in_checkout
    )