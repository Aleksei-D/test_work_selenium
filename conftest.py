
import pytest
from selenium import webdriver

from .setting import BROWSER


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Remote(
        command_executor=f'http://localhost:4444/wd/hub',
        desired_capabilities={'browserName':  f'{BROWSER}'}
    )
    yield browser
    browser.quit()
