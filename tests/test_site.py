from pages.verificationpage import VerPage
from pages.loginpage import LoginPage
from pages.feedpage import FeedPage

def test_login(driver):
    verpage = VerPage(driver)
    verpage.driver_open()
    verpage.phone_number_input()
    verpage.login_button_click()
    loginpage = LoginPage(driver)
    loginpage.login_options()
    loginpage.password_option()
    loginpage.password_option_input()
    loginpage.continue_button()
    feedpage = FeedPage(driver)
    feedpage.login_validation()

    # driver.get("https://vk.com/")
    # wait = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//input[@class="VkIdForm__input"]'))
    # ).send_keys(phone_number)
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//span[text()='Войти']"))
    # ).click()
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, '//span[text()="Подтвердить другим способом"]'))
    # ).click()
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, '//span[text()="Пароль"]'))
    # ).click()
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
    # ).send_keys(password)
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, '//span[text()="Продолжить"]'))
    # ).click()
    # validation = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Моя страница"]')))
    # assert validation is not None



