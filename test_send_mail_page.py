
import allure
from selenium import webdriver

from .pages.mail_page import MailYandexPage
from .setting import EMAIL_LOGIN, EMAIL_PASSWORD, NUMBER_EXPECTED_MAILS, \
    RECIPIENTS_EMAILS, SUBJECT_MAIL_TO_SEARCH, SURE_NAME, URL_SITE


@allure.feature('Test send email by Yandex.Mail')
class TestSendMailPage:

    def test_send_email_by_yandex(self, browser: webdriver.Remote):
        mail_page = MailYandexPage(browser, URL_SITE)
        mail_page.open()
        mail_page.should_be_login_link()

        login_page = mail_page.go_to_login_page()
        login_page.login_yandex_mail(login=EMAIL_LOGIN, password=EMAIL_PASSWORD)

        mail_page = MailYandexPage(browser=browser, url=browser.current_url)
        mail_page.should_be_email_page()

        number_incoming_emails = mail_page.get_number_incoming_mails(search_data=SUBJECT_MAIL_TO_SEARCH)
        assert number_incoming_emails == NUMBER_EXPECTED_MAILS, \
            f'{number_incoming_emails} mails were found, {NUMBER_EXPECTED_MAILS} mails are expected'

        subject_mail_to_send = f'{SUBJECT_MAIL_TO_SEARCH}. {SURE_NAME}'
        message = f'Количество писем - {number_incoming_emails}'

        mail_page.draft_email(recipients=RECIPIENTS_EMAILS, subject=subject_mail_to_send, message=message)
        mail_page.send_email()
