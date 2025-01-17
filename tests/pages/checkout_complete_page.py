from selenium.webdriver.common.by import By

class Checkout_complete:
    def __init__(self, driver):
        self.driver = driver
        self.back_to_button = driver.find_element(By.ID,"back-to-products")

    def back_to_products(self):
        self.back_to_button.click()

        