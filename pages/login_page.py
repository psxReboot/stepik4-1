from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "No correct login url"

    def should_be_login_form(self):
        elements = self.browser.find_elements(*LoginPageLocators.LOGIN_FORM)
        assert len(elements) == 1, "No correct login form on the login page "

    def should_be_register_form(self):
        elements = self.browser.find_elements(*LoginPageLocators.REGISTER_FORM)
        assert len(elements) == 1, "No correct register form on the login page "

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSW1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSW2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()