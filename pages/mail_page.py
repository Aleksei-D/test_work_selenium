import allure
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage
from .login_page import LoginYandexPage
from .locators import MailYandexPageLocators


class MailYandexPage(BasePage):

    @allure.step('Test of transition to the login page')
    def go_to_login_page(self) -> LoginYandexPage:
        link = self.browser.find_element(*MailYandexPageLocators.LINK_LOGIN)
        link.click()
        return LoginYandexPage(browser=self.browser, url=self.browser.current_url)

    @allure.step('Test for getting the number of emails with a subject')
    def get_number_incoming_mails(self, search_data: str) -> int:
        self.should_be_button_incoming_email()
        self.search_email_by_subject(search_data=search_data)
        self.filter_search_result()
        return self.count_the_number_of_elements()

    @allure.step('Email search test with a subject')
    def search_email_by_subject(self, search_data: str) -> None:
        search_input = self.browser.find_element(*MailYandexPageLocators.INPUT_SEARCH)
        search_input.click()
        search_input.clear()
        search_input.send_keys(search_data)
        search_input.send_keys(Keys.RETURN)

    @allure.step('Search results filtering test')
    def filter_search_result(self) -> None:
        self.open_config_search_result()
        self.add_filter_search_result()

    @allure.step('Test of opening the search config')
    def open_config_search_result(self) -> None:
        self.should_be_button_filter_folders()
        button_filter_folder = self.browser.find_element(*MailYandexPageLocators.BUTTON_FILTER_FOLDER)
        button_filter_folder.click()

    @allure.step('Test of adding a filter to search results')
    def add_filter_search_result(self) -> None:
        self.should_be_button_incoming_email()
        button_incoming_email = self.browser.find_element(*MailYandexPageLocators.BUTTON_INCOMING_MAIL)
        button_incoming_email.click()

    @allure.step('Test for counting the number of elements on a page')
    def count_the_number_of_elements(self) -> int:
        incoming_emails = self.browser.find_elements(*MailYandexPageLocators.INCOMING_MAILS)
        return len(incoming_emails)

    @allure.step('Email drafting test')
    def draft_email(self, recipients: list, subject: str, message: str) -> None:
        self.open_modal_window_to_draft_mail()
        self.should_be_elements_in_draft_mail()

        self.enter_email_recipients(recipients=recipients)
        self.enter_email_subject(subject=subject)
        self.enter_email_message(message=message)

    @allure.step('Test of opening a modal window for drafting a email')
    def open_modal_window_to_draft_mail(self) -> None:
        button_write_email = self.browser.find_element(*MailYandexPageLocators.BUTTON_WRITE_MAIL)
        button_write_email.click()

    @allure.step('Send email test')
    def send_email(self):
        button_send = self.browser.find_element(*MailYandexPageLocators.BUTTON_SEND_MAIL)
        button_send.click()

    @allure.step('Enter email recipients test')
    def enter_email_recipients(self, recipients: list) -> None:
        input_recipients_email = self.browser.find_element(*MailYandexPageLocators.INPUT_RECIPIENTS_MAIL)
        input_recipients_email.click()
        recipients_str = ', '.join([rec for rec in recipients])
        input_recipients_email.send_keys(recipients_str)

    @allure.step('Enter email subject test')
    def enter_email_subject(self, subject: str) -> None:
        input_subject_email = self.browser.find_element(*MailYandexPageLocators.INPUT_SUBJECT_MAIL)
        input_subject_email.send_keys(subject)

    @allure.step('Enter email message test')
    def enter_email_message(self, message: str) -> None:
        input_message = self.browser.find_element(*MailYandexPageLocators.INPUT_MESSAGE_BODY)
        input_message.click()
        input_message.send_keys(message)

    @allure.step('Test for the presence of elements on the mail page')
    def should_be_email_page(self) -> None:
        self.should_be_input_search()
        self.should_be_button_incoming_email()
        self.should_be_button_drafting_email()

    @allure.step('Test for the presence of elements on the modal window for drafting a email')
    def should_be_elements_in_draft_mail(self) -> None:
        self.should_be_input_recipients_mail()
        self.should_be_input_subject_mail()
        self.should_be_input_message()
        self.should_be_button_send_mail()

    @allure.step('Test for the presence of the input of mail recipients')
    def should_be_input_recipients_mail(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.INPUT_RECIPIENTS_MAIL), \
            "Input recipients email is not presented"

    @allure.step('Test for the presence of the input of subject')
    def should_be_input_subject_mail(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.INPUT_SUBJECT_MAIL), \
            "Input subject email is not presented"

    @allure.step('Test for the presence of the input of message')
    def should_be_input_message(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.INPUT_MESSAGE_BODY), \
            "Input message is not presented"

    @allure.step('Test for the presence of the button of send email')
    def should_be_button_send_mail(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.BUTTON_SEND_MAIL), \
            "Button send email is not presented"

    @allure.step('Test for the presence of the login link')
    def should_be_login_link(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.LINK_LOGIN), "Login link is not presented"

    @allure.step('Test for the presence of the input search')
    def should_be_input_search(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.INPUT_SEARCH), "Input search is not presented"

    @allure.step('Test for the presence of the button of filter a folders')
    def should_be_button_filter_folders(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.BUTTON_FILTER_FOLDER), \
            "Button filter by folder is not presented"

    @allure.step('Test for the presence of the button of incoming email')
    def should_be_button_incoming_email(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.BUTTON_INCOMING_MAIL),\
            "Button incoming email is not presented"

    @allure.step('Test for the presence of the button of drafting a email')
    def should_be_button_drafting_email(self) -> None:
        assert self.is_element_present(*MailYandexPageLocators.BUTTON_WRITE_MAIL),\
            "Button write email is not presented"
