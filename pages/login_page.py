from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .locators import BasePageLocators
from random_word import RandomWords
import time


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

    def register_new_user(self):
        self.email = (str(time.time()) + "@fakemail.org")
        self.password = (str(time.time()) + "123")
        email_adress = self.browser.find_element(*LoginPageLocators.USER_EMAIL_ADDRESS)
        email_adress.send_keys(self.email)
        reg_password = self.browser.find_element(*LoginPageLocators.USER_PASSWORD)
        reg_password.send_keys(self.password)
        reg_password_1 = self.browser.find_element(*LoginPageLocators.USER_PASSWORD_1)
        reg_password_1.send_keys(self.password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()
