from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


# def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_card()
#     page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


# def test_message_dissapeared_after_adding_product_to_cart(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_card()
#     page.should_not_be_dissapeared_success_message()