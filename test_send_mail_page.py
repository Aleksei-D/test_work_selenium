import shlex
import subprocess

import allure
from selenium import webdriver
import pytest

from .pages.mail_page import MailYandexPage
from .setting import ALLURE_REPORTS_PATH, EMAIL_LOGIN, EMAIL_PASSWORD, NUMBER_EXPECTED_MAILS, \
    RECIPIENTS_EMAILS, SUBJECT_MAIL_TO_SEARCH, SURE_NAME, URL_SITE


@allure.feature('Test send email by Yandex.Mail')
class TestSendMailPage:

    @allure.story('test_login_yandex_mail')
    @allure.severity('critical')
    @pytest.mark.dependency()
    def test_login_yandex_mail(self, browser: webdriver.Remote):
        with allure.step(f'Open page - {URL_SITE}'):
            mail_page = MailYandexPage(browser, URL_SITE)
            mail_page.open()
            with allure.step('Checking the login link'):
                mail_page.should_be_login_link()

        with allure.step('Go to the login page'):
            login_page = mail_page.go_to_login_page()

            with allure.step('Checking the presence of the login input field and entering the login'):
                login_page.should_be_login_input()
                login_page.enter_login(login=EMAIL_LOGIN)

            with allure.step('Checking the presence of password input field and entering the password'):
                login_page.should_be_password_input()
                login_page.enter_password(password=EMAIL_PASSWORD)

    @allure.story('test_present_link_in_main_page')
    @allure.severity('critical')
    @pytest.mark.dependency(depends=['test_login_yandex_mail'])
    def test_present_link_in_main_page(self, browser: webdriver.Remote):
        mail_page = MailYandexPage(browser, browser.current_url)
        mail_page.should_be_email_page()

    @allure.story('test_search_incoming_emails')
    @allure.severity('normal')
    @pytest.mark.dependency(depends=['test_login_yandex_mail'])
    def test_search_incoming_emails(self, browser: webdriver.Remote, request):
        mail_page = MailYandexPage(browser, browser.current_url)
        with allure.step(f'Searching for emails with a subject - {SUBJECT_MAIL_TO_SEARCH}'):
            mail_page.search_email_by_subject(search_data=SUBJECT_MAIL_TO_SEARCH)

            with allure.step(f'Searching for emails with a subject - {SUBJECT_MAIL_TO_SEARCH}'):
                mail_page.should_be_button_filter_folder()
                mail_page.open_config_search_result()

            with allure.step(f'Filter the search result'):
                mail_page.should_be_button_incoming_email()
                mail_page.add_filter_search_result_by_incoming()
                numbers_incoming_mails = mail_page.get_the_number_of_incoming_messages()
                pytest.shared = numbers_incoming_mails
                request.config.cache.set('numbers_incoming_mails', numbers_incoming_mails)
                assert numbers_incoming_mails == NUMBER_EXPECTED_MAILS, \
                    f'{numbers_incoming_mails} mails were found, {NUMBER_EXPECTED_MAILS} mails are expected'

    @allure.story('test_send_yandex_mail')
    @allure.severity('normal')
    @pytest.mark.dependency(depends=['test_login_yandex_mail'])
    def test_send_mail(self, browser: webdriver.Remote, request):
        mail_page = MailYandexPage(browser, browser.current_url)

        with allure.step(f'Opening a modal window for sending the email'):
            mail_page.open_modal_window_to_draft_mail()
            mail_page.should_be_email_page()
            numbers_incoming_mails = request.config.cache.get('numbers_incoming_mails', None)
            subject_mail_to_send = f'{SUBJECT_MAIL_TO_SEARCH}. {SURE_NAME}'
            message = f'Количество писем - {numbers_incoming_mails}'
            with allure.step(f'Sending the email'):
                mail_page.draft_email(recipients=RECIPIENTS_EMAILS, subject=subject_mail_to_send, message=message)
                mail_page.send_email()
