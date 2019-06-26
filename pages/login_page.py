from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url

    def should_be_login_form(self):

        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Email field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Password field is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Email field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD), "Confirm Password field is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTER_BUTTON).click()

    def user_is_logged(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User is not logged in"