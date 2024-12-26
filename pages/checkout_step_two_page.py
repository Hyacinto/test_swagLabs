from selenium.webdriver.common.by import By

class Checkout_step_two:
    def __init__(self, driver):
        self.driver = driver
        self.total_price = float(driver.find_element(By.CSS_SELECTOR,".summary_subtotal_label").text.split(":")[-1].strip().replace("$", ""))
        self.price_checkout = [float(price.text.replace("$", "")) for price in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
        self.description_checkout = [desc.text for desc in driver.find_elements(By.CLASS_NAME, "inventory_item_desc")]
        self.title_checkout =  [title.text for title in driver.find_elements(By.CLASS_NAME,"inventory_item_name")]
        self.finish_button = driver.find_element(By.ID,"finish")
        self.back_to_button = driver.find_element(By.ID,"cancel")

    @property
    def calculate_total_price(self):
        return sum(self.price_checkout,start=0)

    def checkout_finish(self):
        self.finish_button.click()

    def back_to_products(self):
        self.back_to_button.click()

        