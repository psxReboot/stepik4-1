import time
from pages.locators import MainPageLocators
from pages.main_page import MainPage
from pages.login_page import LoginPage

def open_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    browser.find_element(*MainPageLocators.LOGIN_LINK).click()
    login_page = LoginPage(browser, link)
    return login_page

def test_login_page_correct(browser):
    login_page=open_login_page(browser)
    login_page.should_be_login_page()
#def test_login_link_get_valid_url(browser):
#    login_page = open_login_page(browser)
#    login_page.should_be_login_url()

#def test_login_page_have_login_form(browser):
#    login_page = open_login_page(browser)
#    login_page.should_be_login_form()

#def test_login_page_have_register_form(browser):
#    login_page=open_login_page(browser)
#    login_page.should_be_register_form()
