from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_options(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Подтвердить другим способом"]'))
        ).click()

    def password_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Пароль"]'))
        ).click()

    def password_option_input(self):
        load_dotenv()
        password = os.getenv("PASSWORD")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
        ).send_keys(password)

    def continue_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Продолжить"]'))
        ).click()
