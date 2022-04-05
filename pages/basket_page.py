from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):

    # гость не может увидеть товар в корзине, открытой с главной страницы
    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        assert self.browser.find_element(*BasketPageLocators.BUTTON_VIEW_BASKET), "View basket button is not presented"

    # гость не может увидеть товар в корзине, открытой со страницы товара
    def guest_cant_see_product_in_basket_opened_from_product_page(self):
        assert self.browser.find_element(*BasketPageLocators.BUTTON_VIEW_BASKET), "View basket button is not presented"

    # должна быть кнопка просмотра корзины
    def should_be_button_view_basket(self):
        assert self.browser.find_element(*BasketPageLocators.BUTTON_VIEW_BASKET), "View basket button is not presented"

    # должно быть сообщение об отсутствии товара
    def should_be_a_message_the_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_BASKET), "Message the_basket_is_empty "\
                                                                                   "not presented"

    # 'Your basket is empty.' пуста есть в сообщении
    def should_be_text_in_the_message(self):
        message_text = 'Your basket is empty.'
        message = self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_BASKET).text
        assert message_text in message, 'No text in the message'
