
import pytest
from selenium import webdriver

from .setting import PORT_GRID, BROWSER


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Remote(
        command_executor=f'http://127.0.0.1:{PORT_GRID}/wd/hub',
        desired_capabilities={'browserName':  f'{BROWSER}'}
    )
    yield browser
    browser.quit()
