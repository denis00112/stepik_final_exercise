from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()
        self.solve_quiz_and_get_code()

    def should_be_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)

        # реализуйте проверку, что есть форма логина
        assert product_name.text == added_name.text,"Product not in basket"

    def should_be_same_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_VALUE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)

        # реализуйте проверку, что есть форма логина
        assert product_price.text == basket_price.text, "Prices differ"


