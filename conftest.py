import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# run command: pytest -v --tb=line --language=en test_main_page.py
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en or ru")  # default=None


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    time.sleep(300)
    print("\nquit browser..")
    browser.quit()

