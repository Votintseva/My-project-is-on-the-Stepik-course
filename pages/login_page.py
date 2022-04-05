from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .locators import BasePageLocators
from random_word import RandomWords


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # 'login' есть в URL
    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "login is absent in current url"

    # должна быть форма входа
    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    # должна быть форма регистрации
    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        r = RandomWords()
        self.email = r.get_random_word() + "@fakemail.org"
        self.password = r.get_random_word() + "123"
        email = browser.find_element(*LoginPageLocators.USER_EMAIL_ADDRESS, 'input')
        email.send_keys(self.email)
        password = browser.find_element(*LoginPageLocators.USER_PASSWORD, 'input')
        password.ssend_keys(self.password)
