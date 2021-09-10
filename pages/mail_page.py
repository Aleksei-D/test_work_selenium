
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage
from .login_page import LoginYandexPage
from .locators import MailYandexPageLocators


class MailYandexPage(BasePage):

    def go_to_login_page(self) -> LoginYandexPage:
        link = self.browser.find_element(*MailYandexPageLocators.LINK_LOGIN)
        link.click()
        return LoginYandexPage(browser=self.browser, url=self.browser.current_url)

    def search_email_by_subject(self, search_data) -> None:
        search_input = self.browser.find_element(*MailYandexPageLocators.INPUT_SEARCH)
        search_input.click()
        search_input.clear()
        search_input.send_keys(search_data)
        search_input.send_keys(Keys.RETURN)

    def open_config_search_result(self) -> None:
        button_filter_folder = self.browser.find_element(*MailYandexPageLocators.BUTTON_FILTER_FOLDER)
        button_filter_folder.click()

    def add_filter_search_result_by_incoming(self) -> None:
        button_incoming_email = self.browser.find_element(*MailYandexPageLocators.BUTTON_INCOMING_MAIL)
        button_incoming_email.click()

    def get_the_number_of_incoming_messages(self) -> int:
        incoming_emails = self.browser.find_elements(*MailYandexPageLocators.INCOMING_MAILS)
        return len(incoming_emails)

    def open_modal_window_to_draft_mail(self) -> None:
        button_write_email = self.browser.find_element(*MailYandexPageLocators.BUTTON_WRITE_MAIL)
        button_write_email.click()

    def draft_email(self, recipients: list, subject: str, message: str) -> None:
        self.enter_email_recipients(recipients=recipients)
        self.enter_email_subject(subject=subject)
        self.enter_email_message(message=message)

    def send_email(self):
        button_send = self.browser.find_element(*MailYandexPageLocators.BUTTON_SEND_MAIL)
        button_send.click()

    def enter_email_recipients(self, recipients: list) -> None:
        input_recipients_email = self.browser.find_element(*MailYandexPageLocators.INPUT_RECIPIENTS_MAIL)
        input_recipients_email.click()
        recipients_str = ', '.join([rec for rec in recipients])
        input_recipients_email.send_keys(recipients_str)

    def enter_email_subject(self, subject: str):
        input_subject_email = self.browser.find_element(*MailYandexPageLocators.INPUT_SUBJECT_MAIL)
        input_subject_email.send_keys(subject)

    def enter_email_message(self, message: str):
        input_message = self.browser.find_element(*MailYandexPageLocators.INPUT_MESSAGE_BODY)
        input_message.click()
        input_message.send_keys(message)

    def should_be_email_page(self) -> None:
        self.should_be_input_search()
        self.should_be_button_incoming_email()
        self.should_be_button_write_email()

    def should_be_login_modal_window_to_draft_mail(self) -> None:
        self.should_be_input_recipients_mail()
        self.should_be_input_subject_mail()
        self.should_be_input_message()
        self.should_be_button_send_mail()

    def should_be_input_recipients_mail(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.INPUT_RECIPIENTS_MAIL), \
            "Input recipients email is not presented"

    def should_be_input_subject_mail(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.INPUT_SUBJECT_MAIL), \
            "Input subject email is not presented"

    def should_be_input_message(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.INPUT_MESSAGE_BODY), \
            "Input message is not presented"

    def should_be_button_send_mail(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.BUTTON_SEND_MAIL), \
            "Button send email is not presented"

    def should_be_login_link(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.LINK_LOGIN), "Login link is not presented"

    def should_be_input_search(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.INPUT_SEARCH), "Input search is not presented"

    def should_be_button_filter_folder(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.BUTTON_FILTER_FOLDER), \
            "Button filter by folder is not presented"

    def should_be_button_incoming_email(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.BUTTON_INCOMING_MAIL),\
            "Button incoming email is not presented"

    def should_be_button_write_email(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.BUTTON_WRITE_MAIL),\
            "Button write email is not presented"
