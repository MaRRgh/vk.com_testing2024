from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv


def test_vk(driver):
    load_dotenv()
    phone_number = os.getenv("PHONE_NUMBER")
    password = os.getenv("PASSWORD")
    driver.get("https://vk.com/")
    wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@class="VkIdForm__input"]'))
    ).send_keys(phone_number)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Войти']"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Подтвердить другим способом"]'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Пароль"]'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
    ).send_keys(password)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Продолжить"]'))
    ).click()
    validation = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Моя страница"]')))
    assert validation is not None



