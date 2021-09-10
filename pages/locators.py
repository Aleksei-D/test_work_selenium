from selenium.webdriver.common.by import By

from ..setting import SUBJECT_MAIL_TO_SEARCH


class LoginYandexPageLocators:
    INPUT_LOGIN = (By.NAME, 'login')
    INPUT_PASSWORD = (By.NAME, 'passwd')


class MailYandexPageLocators:
    BUTTON_INCOMING_MAIL = (By.XPATH, "//span[contains(text(), 'Входящие')]")
    BUTTON_FILTER_FOLDER = (By.XPATH, "//div[@class='mail-AdvancedSearch']/button[3]")
    BUTTON_SEND_MAIL = (By.XPATH, "//span[contains(text(), 'Отправить')]/ancestor::button[1]")
    BUTTON_WRITE_MAIL = (By.XPATH, "//a[@title='Написать (w, c)']")
    INCOMING_MAILS = (By.XPATH, f"//span[@title='{SUBJECT_MAIL_TO_SEARCH}']")
    INPUT_MESSAGE_BODY = (By.XPATH, "//div[@placeholder='Напишите что-нибудь']/div")
    INPUT_RECIPIENTS_MAIL = (By.CLASS_NAME, 'composeYabbles')
    INPUT_SEARCH = (By.XPATH, "//input[@placeholder='Поиск']")
    INPUT_SUBJECT_MAIL = (By.NAME, 'subject')
    LINK_LOGIN = (By.LINK_TEXT, 'Войти')
