from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def get_usernames(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "login_credentials"))
        )
        credentials = self.driver.find_element(By.ID, "login_credentials").text.split("\n")
        return credentials[1:]  # Az első sor általában cím

    def get_password(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='login_password']"))
        )
        element = self.driver.find_element(By.XPATH, "//div[@class='login_password']")
        return element.text.split(":")[-1].strip()

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

    def has_error_message(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, '*[data-test="error"]')) > 0

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        
