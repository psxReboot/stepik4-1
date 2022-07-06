import time

from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес

        assert "login" in self.browser.current_url, "No correct login url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        elements = self.browser.find_elements(*LoginPageLocators.LOGIN_FORM)
        assert len(elements) == 1, "No correct login form on the login page "

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        elements = self.browser.find_elements(*LoginPageLocators.REGISTER_FORM)
        assert len(elements) == 1, "No correct register form on the login page "

