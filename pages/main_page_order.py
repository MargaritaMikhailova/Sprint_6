import random
import datetime
import re

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from locators import *
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_load_page(self):
        return self.find_element(Element_check.MAIN_PAGE)

    def click_button_order(self):
        self.click(Buttons.BUTTON_ORDER_UP)

    def click_button_in_order(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button_in = self.wait.until(expected_conditions.element_to_be_clickable(Buttons.BUTTON_IN_ORDER))
        self.driver.execute_script("arguments[0].scrollIntoView();", button_in)
        button_in.click()

    def click_button_order_down(self):
        self.click_with_scroll(Buttons.BUTTON_ORDER_DOWN)

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

    def click_button_next(self):
        self.click(Buttons.NEXT_BUTTON)

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

    def pre_req_order(self):
        return self.is_element_visible(Element_check.PRE_REQ_ORDER)

    def click_yes_order(self):
        self.click(Buttons.YES_BUTTON)

    def click_no_order(self):
        self.click(Buttons.NO_BUTTON)

    def click_check_status(self):
        self.click(Buttons.BUTTON_STATUS)

    def check_second_page_form(self):
        return self.find_element(Element_check.SECOND_PAGE_FORM)

    def get_order_number(self):
        order_element = self.find_element(Element_check.SUCCESS_ORDER)

        text = order_element.text
        match = re.search(r'(\d{5,6})', text)
        return match.group(1) if match else "Номер не найден"










