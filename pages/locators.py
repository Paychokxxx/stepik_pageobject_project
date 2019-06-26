from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".btn[value='Register']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESSFULLY_ADDING_ALERTS = (By.CLASS_NAME, "alert-success")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:first-child .alertinner")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages>div:last-child .alertinner > p:first-child")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")


class CartPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.ID, "content_inner")
