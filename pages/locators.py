from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_VALUE = (By.CSS_SELECTOR, ".product_main p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR,".alertinner p strong")

class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_PRODUCT = (By.CSS_SELECTOR, "#basket_formset")