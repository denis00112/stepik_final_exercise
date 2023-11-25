from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Should be empty basket text"

    def should_be_empty(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_PRODUCT), "Basket is not empty"