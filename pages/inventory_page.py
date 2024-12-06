from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class Inventory:
    def __init__(self, driver):
        self.driver = driver
        self.basket = (By.CSS_SELECTOR,"*[data-test='shopping-cart-link']")
        self.links_to_products = self.driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-name']")
        self.prices = self.driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-price']")
        self.select_element = driver.find_element(By.CLASS_NAME, "product_sort_container")
        self.descriptions = driver.find_elements(By.CLASS_NAME, "inventory_item_desc")
        self.dropdown = Select(self.select_element)
        self.add_buttons = driver.find_elements(By.XPATH, "//button[contains(@id, 'add')]")


    @property
    def image_links(self):
        images = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_img img")
        return [img.get_attribute("src") for img in images]
    
    
    def item_counter(self, default=0):
        try:
            return int(self.driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-badge']").text)
        except NoSuchElementException:
            return default
    
    def product_img(self):
        product_img_links = []

        for i in range(len(self.links_to_products)):
            self.links_to_products = self.driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-name']")
            self.links_to_products[i].click()

            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_details_img")))

            img = self.driver.find_element(By.CSS_SELECTOR, ".inventory_details_img")
            img_url = img.get_attribute("src") 
            product_img_links.append(img_url)

            back_to_products = self.driver.find_element(By.ID, "back-to-products")
            back_to_products.click()

            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "inventory_container")))

        return product_img_links
    
    def price_10(self):
        prices = [float(price.text.replace("$", "")) for price in self.prices]
        return sorted(prices, reverse=True)
    
    def price_01(self):
        prices = [float(price.text.replace("$", "")) for price in self.prices]
        return sorted(prices)

    def item_name_ZA(self):
        names = [name.text for name in self.links_to_products]
        return sorted(names, reverse=True)
    
    def item_name_AZ(self):
        names = [name.text for name in self.links_to_products]
        return sorted(names)
    
    def select_AZ(self):
        self.select_element = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        self.dropdown = Select(self.select_element)
        self.dropdown.select_by_index(0)
        WebDriverWait(self.driver, 10).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR, "*[data-test='inventory-item-name']")) )
        self.links_to_products = self.driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-name']")
        return [name.text for name in self.links_to_products]
    
    def select_ZA(self):
        self.select_element = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        self.dropdown = Select(self.select_element)
        self.dropdown.select_by_index(1)
        WebDriverWait(self.driver, 10).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR, "*[data-test='inventory-item-name']")) )
        self.links_to_products = self.driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-name']")
        return [name.text for name in self.links_to_products]
    
    def select_01(self):
        self.select_element = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        self.dropdown = Select(self.select_element)
        self.dropdown.select_by_index(2)
        WebDriverWait(self.driver, 10).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR, "*[data-test='inventory-item-price']")) )
        self.prices = self.driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-price']")
        return [float(price.text.replace("$", "")) for price in self.prices]
    
    def select_10(self):
        self.select_element = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        self.dropdown = Select(self.select_element)
        self.dropdown.select_by_index(3)
        WebDriverWait(self.driver, 10).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR, "*[data-test='inventory-item-price']")) )
        self.prices = self.driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-price']")
        return [float(price.text.replace("$", "")) for price in self.prices]
    
    def description(self):
        price_list = []
        description_list = []
        name_list = []

        for link in self.links_to_products:
            self.links_to_products = self.driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-name']")
            link.click()

            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_desc_container")))

            name = self.driver.find_element(By.CSS_SELECTOR, "*[data-test='inventory-item-name']").text
            name_list.append(name)
            
            description = self.driver.find_element(By.CSS_SELECTOR, "*[data-test='inventory-item-desc']").text
            description_list.append(description)

            price = self.driver.find_element(By.CSS_SELECTOR, "*[data-test='inventory-item-price']").text
            price_list.append(price)

            back_to_products = self.driver.find_element(By.ID, "back-to-products")
            back_to_products.click()

            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "inventory_container")))

        self.links_to_products = self.driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-name']") 
        links = [link.text for link in self.links_to_products]
        self.prices = self.driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-price']")
        prices = [price.text for price in self.prices]
        self.descriptions = self.driver.find_elements(By.CLASS_NAME, "inventory_item_desc")
        descriptions = [desc.text for desc in self.descriptions]

        return price_list, description_list, name_list, links, prices, descriptions

    def basket_in_inventory(self):
        max_attempts = 10
        attempts = 0

        while True:
            self.add_buttons = self.driver.find_elements(By.XPATH, "//button[contains(@id, 'add')]")
   
            if not self.add_buttons:
                break

            self.add_buttons[0].click()

            updated_buttons = self.driver.find_elements(By.XPATH, "//button[contains(@id, 'add')]")
            if len(updated_buttons) == len(self.add_buttons):  
                attempts += 1
                if attempts >= max_attempts:
                    break
        
    def basket_out_inventory(self):
        max_attempts = 10
        attempts = 0

        while True:
            remove_buttons = self.driver.find_elements(By.XPATH, "//button[contains(@id, 'remove')]")
            if not remove_buttons:
                break
            remove_buttons[0].click()

            updated_buttons = self.driver.find_elements(By.XPATH, "//button[contains(@id, 'remove')]")
            if len(updated_buttons) == len(remove_buttons):  
                attempts += 1
                if attempts >= max_attempts:
                    break
        
    def basket_in_item(self):
        for i in range(len(self.links_to_products)):
            self.links_to_products = self.driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-name']")
            self.links_to_products[i].click()

            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_details_img")))

            add_button = self.driver.find_element(By.XPATH, "//button[contains(@id, 'add')]")
            add_button.click()

            back_to_products = self.driver.find_element(By.ID, "back-to-products")
            back_to_products.click()

            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "inventory_container")))
    
    def basket_out_items(self):
        for i in range(len(self.links_to_products)):
            self.links_to_products = self.driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-name']")
            self.links_to_products[i].click()

            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_details_img")))

            add_button = self.driver.find_element(By.XPATH, "//button[contains(@id, 'remove')]")
            add_button.click()

            back_to_products = self.driver.find_element(By.ID, "back-to-products")
            back_to_products.click()

            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "inventory_container")))






    


          


