import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose the language for the browser')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    chrome_options = Options()
    chrome_options.add_argument(f"--lang={language}")
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    print("\nАвтопауза на 5 секунд, чтобы проверить язык кнопки")
    time.sleep(5)
    browser.quit()
