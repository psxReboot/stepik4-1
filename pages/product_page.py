
from .base_page import BasePage
from .locators import ProductPageLocators


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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert  not self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is not presented< but should and then disapper"
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message should disapper but not"
