
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage
from .locators import LoginYandexPageLocators


class LoginYandexPage(BasePage):

    def enter_login(self, login: str):
        login_input = self.browser.find_element(*LoginYandexPageLocators.INPUT_LOGIN)
        login_input.clear()
        login_input.send_keys(login)
        login_input.send_keys(Keys.RETURN)

    def enter_password(self, password: str):
        password_input = self.browser.find_element(*LoginYandexPageLocators.INPUT_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

    def should_be_login_input(self):
        assert self.is_element_present(*LoginYandexPageLocators.INPUT_LOGIN), "Login input is not presented"

    def should_be_password_input(self):
        assert self.is_element_present(*LoginYandexPageLocators.INPUT_PASSWORD), "Password input is not presented"
