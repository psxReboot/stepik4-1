from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM=(By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators:
    BASKET_BUTTON=(By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME_MESSAGES=(By.CSS_SELECTOR,"#messages strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".breadcrumb li.active")
    BOOK_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")

