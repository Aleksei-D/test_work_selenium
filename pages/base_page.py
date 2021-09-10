from selenium import webdriver
from selenium.common.exceptions import InvalidSelectorException


class BasePage:
    def __init__(self, browser: webdriver.Remote, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except InvalidSelectorException:
            return False
        return True
