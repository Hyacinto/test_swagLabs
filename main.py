from selenium import webdriver
from selenium.webdriver.firefox.options import Options   
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from selenium.webdriver.common.by import By


def get_usernames(driver):
    WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "login_credentials"))
    )
    credentials = driver.find_element(By.ID, "login_credentials").text.split("\n")
    return credentials[1:]

def get_password(driver):
    WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='login_password']"))
    )
    element = driver.find_element(By.XPATH, "//div[@class='login_password']")
    return element.text.split(":")[-1].strip()

def get_users_and_their_passwords():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Firefox(options=options)
    driver.get("https://www.saucedemo.com/")

    usernames = get_usernames(driver)
    password = get_password(driver)

    driver.quit()

    with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["username", "password"])
        for i in range(len(usernames)):
            writer.writerow([usernames[i], password])

get_users_and_their_passwords()
        