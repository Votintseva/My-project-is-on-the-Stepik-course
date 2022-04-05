from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .locators import BasePageLocators, ProductPageLocators, BasketPageLocators


class BasePage:
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        # Команда для неявного ожидания со значением по умолчанию в 3

    # открыть страницу
    def open(self):
        self.browser.get(self.url)

    # перейдите на страницу входа в систему
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # перейдите на страницу корзины
    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasketPageLocators.BUTTON_VIEW_BASKET)
        basket_link.click()

    # элемент есть на странице
    def is_element_present(self, how: object, what: object) -> object:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # метод, который проверяет, что элемент не появляется на странице в течение заданного времени:
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # метод, который проверяет, что элемент исчезает:
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # должна быть ссылка для входа в систему
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    #  проверка того, что пользователь залогинен:
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                         " probably unauthorised user"
