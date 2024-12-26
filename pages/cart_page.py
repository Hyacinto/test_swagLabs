from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.utilities import Utilities

class Cart:
    def __init__(self, driver):
       self.driver = driver
       self.prices_cart = Utilities.price_list(driver)
       self.descriptions_cart = Utilities.description_list(driver)
       self.titles_cart =  Utilities.title_list(driver)
       self.checkout_button = driver.find_element(By.ID,"checkout")
       self.continue_button = driver.find_element(By.ID,"continue-shopping")
       self.remove_buttons = driver.find_elements(By.XPATH, "//button[contains(@id, 'remove')]")

    def empty_cart(self):
        for button in self.remove_buttons:
            self.remove_buttons = self.driver.find_elements(By.XPATH, "//button[contains(@id, 'remove')]")
            button.click()

    def item_counter(self, default=0):
        try:
            return int(self.driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-badge']").text)
        except NoSuchElementException:
            return default
        
    def continue_shopping(self):
        self.continue_button.click() 

    def to_the_checkout(self):
        self.checkout_button.click() 
