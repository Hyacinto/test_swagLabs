from selenium.webdriver.common.by import By

class Checkout_step_one:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = driver.find_element(By.ID,"first-name")
        self.last_name_field = driver.find_element(By.ID, "last-name")
        self.postal_code_field = driver.find_element(By.ID, "postal-code")
        self.continue_button = driver.find_element(By.ID, "continue")
        self.cancel_button = driver.find_element(By.ID,"cancel")

    def has_error_message(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, '*[data-test="error"]')) > 0
    
    def fill_the_fields(self,first_name,last_name,postal_code):
        self.first_name_field.send_keys(first_name)
        self.last_name_field.send_keys(last_name)
        self.postal_code_field.send_keys(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def cancel_checkout(self):
        self.cancel_button.click()

    def get_all_fields(self):
        first_name = self.first_name_field.text
        last_name = self.last_name_field.text
        postal_code = self.postal_code_field.text
        return first_name, last_name, postal_code