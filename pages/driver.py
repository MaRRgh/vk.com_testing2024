from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Driver_Stuff:

    def __init__(self):
        self.driver = webdriver.Chrome
        chrome_options = Options()
        chrome_options.add_argument('--headless')

