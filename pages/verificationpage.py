from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

class VerPage:

    def __init__(self, driver):
        self.driver = driver

    def driver_open(self):
        self.driver.get("https://vk.com/")

    def phone_number_input(self):
        load_dotenv()
        phone_number = os.getenv("PHONE_NUMBER")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@class="VkIdForm__input"]'))
        ).send_keys(phone_number)

    def login_button_click(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Войти']"))
        ).click()


