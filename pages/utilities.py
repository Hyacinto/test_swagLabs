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
    def logout(driver):
        logout = (By.ID, "logout_sidebar_link")
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(logout)).click()

    @staticmethod
    def reset(driver):
        reset_app_state = (By.ID, "reset_sidebar_link")
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(reset_app_state)).click()

    @staticmethod
    def open_menu(driver):
        burger_menu = (By.ID, "react-burger-menu-btn")
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(burger_menu)).click()
        menu = (By.ID, "bm-menu")
   
        try:
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(menu))
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
        
     
