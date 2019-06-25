import math
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_card(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_added_to_card(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESSFULLY_ADDING_ALERTS), "Success alert is mising"
        assert len(self.browser.find_elements(*ProductPageLocators.SUCCESSFULLY_ADDING_ALERTS)) == 2, "Number of alerts is not 2"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(answer)
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def success_message(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

    def basket_message(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE).text

    def should_contains_product_name_in_success_message(self, product_name, success_message):
        excepted_message = "{} has been added to your basket.".format(product_name)
        assert excepted_message == success_message, \
            "Success message should contains product name " \
            "\nexcepted_message = {}" \
            "\nsuccess_message = {}".format(excepted_message, success_message)

    def should_contains_product_price_in_basket_total(self, product_price, basket_message):
        excepted_message = "Your basket total is now {}".format(product_price)
        assert excepted_message == basket_message, \
            "Basket message should contains product price " \
            "\nexcepted_message = {}" \
            "\nbasket_message = {}".format(excepted_message, basket_message)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_dissapeared_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"