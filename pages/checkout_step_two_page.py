from selenium.webdriver.common.by import By
from pages.utilities import Utilities

class Checkout_step_two:
    def __init__(self, driver):
        self.driver = driver
        self.total_price = float(driver.find_element(By.CSS_SELECTOR,".summary_subtotal_label").text.split(":")[-1].strip().replace("$", ""))
        self.price_checkout = Utilities.price_list(driver)
        self.description_checkout = Utilities.description_list(driver)
        self.title_checkout =  Utilities.title_list(driver)
        self.finish_button = driver.find_element(By.ID,"finish")
        self.back_to_button = driver.find_element(By.ID,"cancel")

    @property
    def calculate_total_price(self):
        return sum(self.price_checkout,start=0)

    def checkout_finish(self):
        self.finish_button.click()

    def back_to_products(self):
        self.back_to_button.click()

        