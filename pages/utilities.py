from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utilities:
    def __init__(self, driver):
        self.driver = driver
        self.burger_menu = (By.ID, "react-burger-menu-btn")

    @staticmethod
    def logout(driver):
        burger_menu = (By.ID, "react-burger-menu-btn")
        driver.find_element(*burger_menu).click()
        logout_button = (By.ID, "logout_sidebar_link")
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable(logout_button)
        ).click()
