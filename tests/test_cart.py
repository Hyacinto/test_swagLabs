import pytest
from pages.utilities import Utilities
from pages.inventory_page import Inventory
from pages.cart_page import Cart

def way_to_the_cart(driver,username, password, login_page):
    login_page.login(username, password) 

    inventory_page = Inventory(driver)
    inventory_page.basket_in_inventory()
    inventory_page.to_the_cart()

    cart_page = Cart(driver)
    return cart_page.titles_cart, cart_page.descriptions_cart, cart_page.prices_cart

def test_items_are_the_same(username, setup_teardown):
    driver, login_page, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()

    login_page.login(username, password)

    inventory_page = Inventory(driver)
    inventory_page.basket_in_inventory()
    names_added,descriptions_added,prices_added = inventory_page.items_added_to_the_basket()
    inventory_page.to_the_cart()

    cart_page = Cart(driver)

    assert (
        names_added == cart_page.titles_cart
        and descriptions_added == cart_page.descriptions_cart
        and prices_added == cart_page.prices_cart
    )

def test_remove_items_from_cart(username, setup_teardown):
    driver, login_page, password = setup_teardown

    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")

    login_page.login(username, password)

    inventory_page = Inventory(driver)
    inventory_page.basket_in_inventory()
    inventory_page.to_the_cart()

    cart_page = Cart(driver)
    cart_page.empty_cart()

    assert Utilities.item_counter(driver) == 0

def test_neverending_shoping(username, setup_teardown):
    driver, login_page, _, password = setup_teardown

    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")

    login_page.login(username, password) 

    inventory_page = Inventory(driver)
    inventory_page.basket_in_inventory()
    inventory_page.to_the_cart()

    cart_page = Cart(driver)
    cart_page.continue_shopping()

    expected_URL = "https://www.saucedemo.com/inventory.html"
    actual_URL = driver.current_url

    assert actual_URL == expected_URL

def test_checkout_with_empty_cart(username, setup_teardown):
    driver, login_page, password = setup_teardown

    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")

    login_page.login(username, password) 

    inventory_page = Inventory(driver)
    inventory_page.to_the_cart()

    cart_page = Cart(driver)
    cart_page.to_the_checkout()

    expected_URL = "https://www.saucedemo.com/cart.html"
    actual_URL = driver.current_url

    assert actual_URL == expected_URL

def test_items_in_the_cart_after_logout(username, setup_teardown):
    driver, login_page, password = setup_teardown

    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")

    titles_before_logout, descriptions_before_logout, prices_before_logout = to_the_cart(driver,username, password, login_page)
    counter_before_logout = Utilities.item_counter(driver)

    Utilities.open_menu(driver)
    Utilities.logout(driver)

    titles_after_logout, descriptions_after_logout, prices_after_logout = to_the_cart(driver,username, password, login_page)
    counter_after_logout = Utilities.item_counter(driver)

    assert (
        titles_before_logout == titles_after_logout
        and descriptions_before_logout == descriptions_after_logout
        and prices_before_logout == prices_after_logout
        and counter_before_logout == counter_after_logout
    )
