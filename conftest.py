import time

import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption("--language", action='store', default='ru', help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    browser_language=request.config.getoption("language")
    browser=webdriver.Chrome()
    browser.get(f"http://selenium1py.pythonanywhere.com/{browser_language}/catalogue/coders-at-work_207/")
    yield browser
    time.sleep(5)
    browser.quit()