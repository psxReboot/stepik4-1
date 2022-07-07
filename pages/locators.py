from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")

class MainPageLocators:
    LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")
    BASKET = (By.CSS_SELECTOR, "#default > header > div.navbar.primary.navbar-static-top.navbar-inverse > div > a")

class LoginPageLocators:
    LOGIN_FORM=(By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSW1 = (By.ID, "id_registration-password1")
    REGISTER_PASSW2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name = registration_submit]")

class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")
    BASKET_BUTTON=(By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME_MESSAGES=(By.CSS_SELECTOR,"#messages strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".breadcrumb li.active")
    BOOK_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")

class BasketPageLocators:
    ITEMSTOBUY=(By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs > div > h2")
    EMPTYMESSAGE=(By.CSS_SELECTOR, "#content_inner > p")
