from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.usernames = self.driver.find_element(By.ID, "login_credentials").text.split("\n")[1:]
        self.password = (By.CSS_SELECTOR, ".login_password").text
        
    def enter_username(self, username):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 1).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def error_message(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, '*[data-test="error"]' )) > 0
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button(self)

