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



