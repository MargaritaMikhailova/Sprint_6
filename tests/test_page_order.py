import time
import pytest
import allure
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Element_check
from pages.main_page_order import OrderPage


class TestPageOrder:

    @allure.title('Проверка создания заявки на аренду самоката через верхнюю кнопку "Заказать"')
    @allure.description('Созадние заказа через верхнюю кнопку "Заказать"')
    def test_page(self, driver):
        order_page = OrderPage(driver)

        order_page.wait_for_load_page()
        order_page.click_button_order()
        order_page.fill_order_first_page()
        order_page.click_button_next()
        order_page.fill_order_second_page()
        order_page.click_button_in_order()

        modal = order_page.pre_req_order()
        assert modal.is_displayed()

        order_page.click_yes_order()

        time.sleep(1)

        order_number = self.get_order_number(driver)

        print(f"Номер заказа: {order_number}")

        allure.attach(str(order_number), "Номер заказа", allure.attachment_type.TEXT)

    def get_order_number(self, driver):
        long_wait = WebDriverWait(driver, 60)
        order_element = long_wait.until(EC.visibility_of_element_located(Element_check.SUCCESS_ORDER))

        text = order_element.text
        match = re.search(r'(\d{5,6})', text)

        if match:
            return match.group(1)
        else:
            return "Номер не найден"

    @allure.title('Проверка создания заявки на аренду самоката через нижнюю кнопку "Заказать"')
    @allure.description('Созадние заказа через нижнюю кнопку "Заказать", и отмена создания заказа')
    def test_page_order(self, driver):
        order_page = OrderPage(driver)

        order_page.wait_for_load_page()
        order_page.click_button_order_down()
        order_page.fill_order_first_page()
        order_page.click_button_next()
        order_page.fill_order_second_page()
        order_page.click_button_in_order()
        order_page.pre_req_order()

        order_page.click_no_order()

        second_page_order = order_page.check_second_page_form()
        assert second_page_order.is_displayed()

