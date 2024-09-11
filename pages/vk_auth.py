import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VKLogin:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def login(self):
        load_dotenv()
        password = os.getenv("PASSWORD")
        phone_number = os.getenv("PHONE_NUMBER")
        self.driver.get("https://vk.com/")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@class="VkIdForm__input"]'))
        ).send_keys(phone_number)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Войти']"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Подтвердить другим способом"]'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Пароль"]'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
        ).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Продолжить"]'))
        ).click()

    def login_valid(self):
        validation = WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Моя страница"]'))
        )
        assert validation is not None

    def exit(self):
        self.driver.quit()