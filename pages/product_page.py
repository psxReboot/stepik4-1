import time
from selenium import webdriver
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
class ProductPage(BasePage):

    def add_to_basket_and_check(self):
        self.open_product_page()
        self.add_to_basket()
        self.check_added_book_name()
        self.check_added_book_price()

    def open_product_page(self):
        self.browser.get(self.url)

    def add_to_basket(self):
        self.open_product_page()
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def check_added_book_name(self):
        book_name_messages = self.browser.find_element(*ProductPageLocators.BOOK_NAME_MESSAGES).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name == book_name_messages, "Something wrong with product name"

    def check_added_book_price(self):
        book_price_messages = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_MESSAGE).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert book_price == book_price_messages, "Something wrong with product price"

#browser=webdriver.Chrome()
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#product_page=ProductPage(browser, link)
#product_page.add_to_basket()
##time.sleep(10)
#product_page.check_added_book_name()
#product_page.check_added_book_price()