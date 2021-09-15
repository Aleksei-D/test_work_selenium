
import allure
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage
from .locators import LoginYandexPageLocators


class LoginYandexPage(BasePage):

    @allure.step('Mail authorization test')
    def login_yandex_mail(self, login: str, password: str):
        self.enter_login(login=login)
        self.enter_password(password=password)

    @allure.step('Login input test')
    def enter_login(self, login: str):
        self.should_be_login_input()
        login_input = self.browser.find_element(*LoginYandexPageLocators.INPUT_LOGIN)
        login_input.clear()
        login_input.send_keys(login)
        login_input.send_keys(Keys.RETURN)

    @allure.step('Password input test')
    def enter_password(self, password: str):
        self.should_be_password_input()
        password_input = self.browser.find_element(*LoginYandexPageLocators.INPUT_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

    @allure.step('Test for the presence of a login input field')
    def should_be_login_input(self):
        assert self.is_element_present(*LoginYandexPageLocators.INPUT_LOGIN), "Login input is not presented"

    @allure.step('Test for the presence of a password input field')
    def should_be_password_input(self):
        assert self.is_element_present(*LoginYandexPageLocators.INPUT_PASSWORD), "Password input is not presented"
