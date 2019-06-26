from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_not_be_products(self):
        assert self.is_not_element_present(
            *CartPageLocators.BASKET_ITEMS), "Basket is not empty"

    def should_be_text_about_empty_cart(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_BASKET_MESSAGE),\
            "Message about empty basket is not presented"
