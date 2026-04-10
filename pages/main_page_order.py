import random
import datetime

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from locators import *


class OrderPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.long_wait = WebDriverWait(driver, 30)

    def wait_for_load_page(self):
        return self.wait.until(EC.visibility_of_element_located(Element_check.MAIN_PAGE))

    def click_button_order(self):
        button_up = self.wait.until(EC.visibility_of_element_located(Buttons.BUTTON_ORDER_UP))
        button_up.click()

    def click_button_in_order(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button_in = self.wait.until(expected_conditions.element_to_be_clickable(Buttons.BUTTON_IN_ORDER))
        self.driver.execute_script("arguments[0].scrollIntoView();", button_in)
        button_in.click()

    def click_button_order_down(self):
        button_down = self.long_wait.until(expected_conditions.element_to_be_clickable(Buttons.BUTTON_ORDER_DOWN))
        self.driver.execute_script("arguments[0].scrollIntoView();", button_down)
        self.driver.execute_script("arguments[0].click();", button_down)

    def fill_order_first_page(self):
        name_field = self.wait.until(expected_conditions.element_to_be_clickable(Fill_order.NAME))
        name_field.send_keys("Тест")

        surname_field = self.wait.until(EC.visibility_of_element_located(Fill_order.SURNAME))
        surname_field.send_keys("Тестовыич")

        user_address = f"Москва{random.randint(3, 999)}"
        address_field = self.wait.until(EC.visibility_of_element_located(Fill_order.ADDRESS))
        address_field.send_keys(user_address)

        user_subway = self.wait.until(EC.element_to_be_clickable(Fill_order.SUBWAY))
        user_subway.click()
        subway_button = self.wait.until(EC.element_to_be_clickable(Buttons.BUTTON_SUBWAY))
        subway_button.click()

        user_number = f"+79{random.randint(100000000, 999999999)}"
        number_field = self.wait.until(EC.visibility_of_element_located(Fill_order.NUMBER))
        number_field.send_keys(user_number)

    def click_button_next(self):
        button_up = self.wait.until(EC.visibility_of_element_located(Buttons.NEXT_BUTTON))
        button_up.click()

    def fill_order_second_page(self):

        date_field = self.wait.until(EC.visibility_of_element_located(Fill_order.DATE))
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        formatted_date = tomorrow.strftime("%d.%m.%Y")
        date_field.send_keys(formatted_date)
        date_field.send_keys(Keys.ENTER)

        user_rent = self.wait.until(EC.element_to_be_clickable(Fill_order.LONG_PERIOD))
        user_rent.click()
        type_rent = self.wait.until(EC.element_to_be_clickable(Fill_order.TYPE_RENT))
        type_rent.click()

        type_color = self.wait.until(EC.element_to_be_clickable(Fill_order.TYPE_COLOR))
        self.driver.execute_script("arguments[0].scrollIntoView();", type_color)
        type_color.click()

        user_comment = self.wait.until(EC.visibility_of_element_located(Fill_order.COMMENT))
        user_comment.send_keys("Автотест")

    def pre_req_order(self):
        return self.wait.until(EC.visibility_of_element_located(Element_check.PRE_REQ_ORDER))

    def click_yes_order(self):
        button_yes_order = self.wait.until(EC.visibility_of_element_located(Buttons.YES_BUTTON))
        button_yes_order.click()

    def click_no_order(self):
        button_no_order = self.wait.until(EC.visibility_of_element_located(Buttons.NO_BUTTON))
        button_no_order.click()

    def click_check_status(self):
        button_up = self.wait.until(EC.visibility_of_element_located(Buttons.BUTTON_STATUS))
        button_up.click()

    def check_second_page_form(self):
        return self.wait.until(EC.visibility_of_element_located(Element_check.SECOND_PAGE_FORM))

    def check_logotype_samokat(self, wait_for_load_page):
        logotype_samokat = self.wait.until(EC.element_to_be_clickable(Buttons.BUTTON_LOGOTYPE))
        logotype_samokat.click()
        return wait_for_load_page

    def click_logotype_yandex(self):
        logotype_yandex = self.wait.until(EC.element_to_be_clickable(Buttons.BUTTON_YANDEX))
        logotype_yandex.click()
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self.wait.until(EC.url_contains("https://dzen.ru/"))









