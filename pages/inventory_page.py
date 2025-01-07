from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.utilities import Utilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class Inventory:
    def __init__(self, driver):
        self.driver = driver
        self.basket = driver.find_element(By.CSS_SELECTOR,"*[data-test='shopping-cart-link']")
        self.links_to_products = driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-name']")
        self.prices_inventory = Utilities.price_list(driver)
        self.select_element = driver.find_element(By.CLASS_NAME, "product_sort_container")
        self.descriptions_inventory = Utilities.description_list(driver)
        self.titles_inventory = Utilities.title_list(driver)
        self.dropdown = Select(self.select_element)
        self.add_buttons = driver.find_elements(By.XPATH, "//button[contains(@id, 'add')]")


    @property
    def image_links(self):
        images = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_img img")
        return [img.get_attribute("src") for img in images]
    
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
    
    def expected_list(self,list,is_reverse):
        return sorted(list, reverse=is_reverse)        
        
    def select(self,index,element, driver):
        self.select_element = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        self.dropdown = Select(self.select_element)
        self.dropdown.select_by_index(index)

        try:
            alert = driver.switch_to.alert
            alert.accept()
 
        except NoAlertPresentException:
            WebDriverWait(self.driver, 10).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR, f"*[data-test='inventory-item-{element}']")) )
            list = self.driver.find_elements(By.CSS_SELECTOR, f"*[data-test='inventory-item-{element}']")
            if element == "price": return [float(price.text.replace("$", "")) for price in list]
            return [name.text for name in list]

    def price_converter(self):

        try:
            price = float(self.driver.find_element(By.CSS_SELECTOR, "*[data-test='inventory-item-price']").text.replace("$", ""))
        except ValueError:
            return False
        
        return price
    
    def description(self):
        prices_item_page = []
        descriptions_item_page = []
        names_item_page = []

        initial_links = self.driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-name']")
        for i in range(len(initial_links)):
        
            current_links = self.driver.find_elements(By.CSS_SELECTOR, "*[data-test='inventory-item-name']")
            current_links[i].click()

            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_details_desc_container")))

            name = self.driver.find_element(By.CSS_SELECTOR, "*[data-test='inventory-item-name']").text
            description = self.driver.find_element(By.CSS_SELECTOR, "*[data-test='inventory-item-desc']").text
            price = self.price_converter()
            names_item_page.append(name)
            descriptions_item_page.append(description)
            prices_item_page.append(price)

            back_to_products = self.driver.find_element(By.ID, "back-to-products")
            back_to_products.click()

            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "inventory_container")))

        return prices_item_page, descriptions_item_page, names_item_page

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

            try:
                remove_button = self.driver.find_element(By.XPATH, "//button[contains(@id, 'remove')]")
                remove_button.click()
            except NoSuchElementException:
                print("The Remove button not found, skipping")
        

            back_to_products = self.driver.find_element(By.ID, "back-to-products")
            back_to_products.click()

            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "inventory_container")))

    def to_the_cart(self):
        self.basket.click()

    def items_added_to_the_basket(self):

        containers = self.driver.find_elements(By.CLASS_NAME, "inventory_item_description")

        name = []
        description = []
        price = []

        for container in containers:
            
            if "Remove" in container.text:

                item_name = container.find_element(By.CLASS_NAME, "inventory_item_name").text
                name.append(item_name)

                item_description = container.find_element(By.CLASS_NAME, "inventory_item_desc").text
                description.append(item_description)
                
                item_price = float(container.find_element(By.CLASS_NAME, "inventory_item_price").text.replace("$", ""))
                price.append(item_price)

        with open("items_in_basket.txt", "w") as file:
            for item in name:
                file.write(item + "\n")

        return name,description,price

    def main_conatiner(self):
        return self.driver.find_element(By.ID, "inventory_container")









    


          


