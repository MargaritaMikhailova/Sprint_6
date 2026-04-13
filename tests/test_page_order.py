import time
import pytest
import allure
import re

from pages.main_page_order import OrderPage
from data import ButtonData


class TestPageOrder:

    @allure.title('Проверка создания заявки на аренду самоката через верхнюю кнопку "Заказать"')
    @allure.description('Созадние заказа через верхнюю кнопку "Заказать"')
    @pytest.mark.parametrize("button_method, button_name", ButtonData.BUTTON_PARAMS)
    def test_page(self, driver, button_method, button_name):
        order_page = OrderPage(driver)

        order_page.wait_for_load_page()
        getattr(order_page, button_method)()
        order_page.fill_order_first_page()
        order_page.click_button_next()
        order_page.fill_order_second_page()
        order_page.click_button_in_order()

        modal = order_page.pre_req_order()
        assert modal.is_displayed()

        order_page.click_yes_order()

        time.sleep(1)

        order_number = order_page.get_order_number()

        print(f"Номер заказа: {order_number}")

        allure.attach(str(order_number), "Номер заказа", allure.attachment_type.TEXT)


    @allure.title('Проверка создания заявки на аренду самоката через нижнюю кнопку "Заказать"')
    @allure.description('Созадние заказа через нижнюю кнопку "Заказать", и отмена создания заказа')
    @pytest.mark.parametrize("button_method, button_name", ButtonData.BUTTON_PARAMS)
    def test_page_order(self, driver, button_method, button_name):
        order_page = OrderPage(driver)

        order_page.wait_for_load_page()
        getattr(order_page, button_method)()
        order_page.fill_order_first_page()
        order_page.click_button_next()
        order_page.fill_order_second_page()
        order_page.click_button_in_order()
        order_page.pre_req_order()

        order_page.click_no_order()

        second_page_order = order_page.check_second_page_form()
        assert second_page_order.is_displayed()

