import pytest
from pages.utilities import Utilities
from pages.inventory_page import Inventory
from PIL import Image
import imagehash
import requests
from io import BytesIO

def get_image_hash(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return imagehash.average_hash(img)

def check_duplicate_images(image_links):
    hashes = [get_image_hash(link) for link in image_links]
    return len(hashes) != len(set(hashes))

def test_unique_item_img(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
    login_page.login(username, password) 
    inventory_page = Inventory(driver)
    image_links = inventory_page.image_links
    assert not check_duplicate_images(image_links)

def test_inventory_page_img_vs_product_page_img(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
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
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
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
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
    login_page.login(username, password)

    inventory_page = Inventory(driver)

    assert (
    inventory_page.expected_list(inventory_page.titles_inventory,False) == inventory_page.select(0,"name", driver) 
    and inventory_page.expected_list(inventory_page.titles_inventory,True) == inventory_page.select(1,"name", driver)
    and inventory_page.expected_list(inventory_page.prices_inventory,False) == inventory_page.select(2,"price", driver)
    and inventory_page.expected_list(inventory_page.prices_inventory,True) == inventory_page.select(3,"price", driver)
    )

def test_inventory_page_desc_vs_product_page_desc(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
    login_page.login(username, password)

    inventory_page = Inventory(driver)  
    prices_item_page, descriptions_item_page, names_item_page = inventory_page.description()

    assert(
        prices_item_page == inventory_page.prices_inventory
        and descriptions_item_page == inventory_page.descriptions_inventory
        and names_item_page == inventory_page.titles_inventory
    )

def test_put_items_in_basket_at_inventory_page(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
    login_page.login(username, password)

    inventory_page = Inventory(driver)
    inventory_page.basket_in_inventory()
    actual_result = Utilities.item_counter(driver)
    expected_result = 6

    assert actual_result == expected_result

def test_take_out_items_from_basket_at_inventory_page(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
    login_page.login(username, password)

    inventory_page = Inventory(driver)
    inventory_page.basket_in_inventory()
    inventory_page.basket_out_inventory()

    actual_result = Utilities.item_counter(driver)
    expected_result = 0

    assert actual_result == expected_result

def test_put_items_in_basket_at_product_page(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()
    login_page.login(username, password)

    inventory_page = Inventory(driver)
    inventory_page.basket_in_item()
    actual_result = Utilities.item_counter(driver)
    expected_result = 6

    assert actual_result == expected_result

def test_take_out_items_from_basket_at_product_page(username, setup_teardown):
    driver, login_page, _, password = setup_teardown
    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()

    login_page.login(username, password)

    inventory_page = Inventory(driver)
    inventory_page.basket_in_item()
    inventory_page.basket_out_items()

    actual_result = Utilities.item_counter(driver)
    expected_result = 0

    assert actual_result == expected_result

def test_side_bar_about(username, setup_teardown):
    driver, login_page, _, password = setup_teardown

    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()

    login_page.login(username, password)

    Utilities.open_menu(driver)
    Utilities.about(driver)

    expected_URL = "https://saucelabs.com/"
    actual_URL = driver.current_url

    driver.back()

    assert actual_URL == expected_URL

def test_side_bar_all_items(username, setup_teardown):
    driver, login_page, _, password = setup_teardown

    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()

    login_page.login(username, password)

    inventory_page = Inventory(driver)
    inventory_page.to_the_cart()

    Utilities.open_menu(driver)
    Utilities.all_items(driver)

    expected_URL = "https://www.saucedemo.com/inventory.html"
    actual_URL = driver.current_url

    assert actual_URL == expected_URL

def test_after_reset_there_is_no_remove_button(username, setup_teardown):
    driver, login_page, _, password = setup_teardown

    if username == "locked_out_user":
        pytest.fail(f"Test failed intentionally for user: {username}")
        driver.quit()

    login_page.login(username, password)

    inventory_page = Inventory(driver)
    inventory_page.basket_in_inventory()
    containers_text = inventory_page.main_conatiner().text
    item_counter = Utilities.item_counter(driver)
    
    Utilities.open_menu(driver)
    Utilities.reset(driver)
    Utilities.logout(driver)

    assert "Remove" not in containers_text and item_counter == 0
    


    
    

