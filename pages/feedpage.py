from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FeedPage:

    def __init__(self, driver):
        self.driver = driver

    def login_validation(self):
        login_validation = WebDriverWait(self.driver, 3).until(
            EC.lo((By.XPATH, '//span[text()="Моя страница"]')))
        assert login_validation is not None