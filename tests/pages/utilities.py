from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

class Utilities:
    def __init__(self, driver):
        self.driver = driver
        self.burger_menu = (By.ID, "react-burger-menu-btn")

    @staticmethod
    def has_error_message(driver):
        return len(driver.find_elements(By.CSS_SELECTOR, '*[data-test="error"]')) > 0
    
    
    @staticmethod
    def logout(driver):
        logout = (By.ID, "logout_sidebar_link")
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(logout)).click()

    @staticmethod
    def reset(driver):
        reset_app_state = (By.ID, "reset_sidebar_link")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(reset_app_state))
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((reset_app_state))).click()

    @staticmethod
    def about(driver):
        about = (By.ID, "about_sidebar_link")
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(about)).click()

    @staticmethod
    def all_items(driver):
        all_items = (By.ID, "inventory_sidebar_link")
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(all_items)).click()

    @staticmethod
    def open_menu(driver):
        burger_menu = (By.ID, "react-burger-menu-btn")
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(burger_menu)).click()
        menu = (By.ID, "bm-menu")
   
        try:
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable(menu))
        except TimeoutException:
            print("The menu is not clickable")
            return 
    
        driver.find_element(*menu).click()

    @staticmethod
    def item_counter(driver, default=0):
        try:
            return int(driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-badge']").text)
        except NoSuchElementException:
            return default
        
    @staticmethod
    def price_list(driver):
        return [float(price.text.replace("$", "")) for price in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
    
    @staticmethod
    def description_list(driver):
        return [desc.text for desc in driver.find_elements(By.CLASS_NAME, "inventory_item_desc")]
    
    @staticmethod
    def title_list(driver):
        return [title.text for title in driver.find_elements(By.CLASS_NAME,"inventory_item_name")]
    
    @staticmethod
    def social_media_icons(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        social = driver.find_element(By.CLASS_NAME, "social")
        return social.is_displayed()
    