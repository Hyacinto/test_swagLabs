import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.login_page import Login
from pages.utilities import Utilities
from pages.inventory_page import Inventory
from PIL import Image
import imagehash
import requests
from io import BytesIO

# Helper function to initialization of Selenium and the data extraction
def get_user_data():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.saucedemo.com/")
    login_page = Login(driver)
    usernames = login_page.get_usernames()  # Fetch usernames
    password = login_page.get_password()    # Fetch password
    driver.quit()  # Close browser after data extraction
    return usernames, password

def get_image_hash(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return imagehash.average_hash(img)

def check_duplicate_images(image_links):
    hashes = [get_image_hash(link) for link in image_links]
    return len(hashes) != len(set(hashes))

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

    Utilities.open_menu(driver)
    Utilities.reset(driver)
    Utilities.logout(driver)
    driver.quit()

# Dynamic parametering

def pytest_generate_tests(metafunc):
    if "username" in metafunc.fixturenames:
        usernames, _ = get_user_data()  # Only extract usernames
        metafunc.parametrize("username", usernames)

# Test functions
def test_unique_item_img(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    login_page.login(username, password) 
    inventory_page = Inventory(driver)
    image_links = inventory_page.image_links
    assert not check_duplicate_images(image_links)

def test_inventory_page_img_vs_product_page_img(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    login_page.login(username, password)
    inventory_page = Inventory(driver)
    image_links = inventory_page.image_links
    product_img_list = inventory_page.product_img()

    for i in range(len(image_links)):
        inventory_img_url = image_links[i]
        product_img_url = product_img_list[i] 
        
        inventory_img_hash = get_image_hash(inventory_img_url)
        product_img_hash = get_image_hash(product_img_url)
        
        assert inventory_img_hash == product_img_hash

def test_visual(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    login_page.login(username, password)

    base_img_path = "base_screenshot.png"
    actual_img_path = f"{username}_screenshot.png"

    if username == "standard_user":
        driver.save_screenshot(base_img_path)
    else:
        driver.save_screenshot(actual_img_path)

    if username != "standard_user":
        base_image = Image.open(base_img_path)
        actual_image = Image.open(actual_img_path)
        
        assert base_image == actual_image

def test_selector_menu(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    login_page.login(username, password)

    inventory_page = Inventory(driver)

    assert (
    inventory_page.expected_list("name",False) == inventory_page.select(0,"name") 
    and inventory_page.expected_list("name",True) == inventory_page.select(1,"name")
    and inventory_page.expected_list("price",False) == inventory_page.select(2,"price")
    and inventory_page.expected_list("price",True) == inventory_page.select(3,"price")
    )

def test_inventory_page_desc_vs_product_page_desc(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    login_page.login(username, password)

    inventory_page = Inventory(driver)  
    price_list, description_list, name_list, links, prices, descriptions = inventory_page.description()

    assert(
        price_list == prices
        and description_list == descriptions
        and name_list == links
    )

def test_put_items_in_basket_at_inventory_page(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    login_page.login(username, password)

    inventory_page = Inventory(driver)
    inventory_page.basket_in_inventory()
    actual_result = inventory_page.item_counter()
    expected_result = 6

    assert actual_result == expected_result

def test_take_out_items_from_basket_at_inventory_page(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    login_page.login(username, password)

    inventory_page = Inventory(driver)
    inventory_page.basket_in_inventory()
    inventory_page.basket_out_inventory()
    actual_result = inventory_page.item_counter()
    expected_result = 0

    assert actual_result == expected_result

def test_put_items_in_basket_at_product_page(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    login_page.login(username, password)

    inventory_page = Inventory(driver)
    inventory_page.basket_in_item()
    actual_result = inventory_page.item_counter()
    expected_result = 6

    assert actual_result == expected_result

def test_take_out_items_from_basket_at_product_page(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    login_page.login(username, password)

    inventory_page = Inventory(driver)
    inventory_page.basket_in_item()
    inventory_page.basket_out_items()
    actual_result = inventory_page.item_counter()
    expected_result = 0

    assert actual_result == expected_result

