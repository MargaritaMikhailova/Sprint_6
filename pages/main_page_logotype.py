import pytest
import random
import datetime

from data import Urls
from locators import *
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class LogotypePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_load_page(self):
        return self.find_element(Element_check.MAIN_PAGE)

    def click_button_order_down(self):
        self.click_with_scroll(Buttons.BUTTON_ORDER_DOWN)

    def click_button_order(self):
        self.click(Buttons.BUTTON_ORDER_UP)

    def fill_order_first_page(self):
        name = ("Тест")
        self.input_text(Fill_order.NAME, name)

        surname = ("Тестовыич")
        self.input_text(Fill_order.SURNAME, surname)

        address = f"Москва{random.randint(3, 999)}"
        self.input_text(Fill_order.ADDRESS, address)

        self.click(Fill_order.SUBWAY)
        self.click(Buttons.BUTTON_SUBWAY)

        user_number = f"+79{random.randint(100000000, 999999999)}"
        self.input_text(Fill_order.NUMBER, user_number)

    def fill_order_second_page(self):
        date_field = self.find_element(Fill_order.DATE)
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        formatted_date = tomorrow.strftime("%d.%m.%Y")
        date_field.send_keys(formatted_date)
        date_field.send_keys(Keys.ENTER)

        self.click(Fill_order.LONG_PERIOD)
        self.click(Fill_order.TYPE_RENT)

        self.click_with_scroll(Fill_order.TYPE_COLOR)

        user_comment = ("Автотест")
        self.input_text(Fill_order.COMMENT, user_comment)

    def click_button_next(self):
        self.click(Buttons.NEXT_BUTTON)

    def check_logotype_samokat(self):
        self.click(Buttons.BUTTON_LOGOTYPE)
        return self.wait_for_load_page()

    def click_logotype_yandex(self):
        self.click(Buttons.BUTTON_YANDEX)
        self.switch_to_new_window()
        return self.wait_for_url_contains(Urls.DZEN_PAGE)
