from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_shoud_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTYMESSAGE), "guest see that basket is not empty"

    def shoud_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMSTOBUY), "guest see item(s) in basket"