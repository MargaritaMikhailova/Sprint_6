import pytest
import allure

from pages.main_page_order import OrderPage

class TestLogo:

    @allure.title('Проверить логотип "Самокат"')
    @allure.description('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката». после заполение первой части')
    def test_logotype_check_one(self, driver):
        order_page = OrderPage(driver)

        order_page.wait_for_load_page()
        order_page.click_button_order()
        order_page.fill_order_first_page()

        logotype_samokat = order_page.check_logotype_samokat(order_page.wait_for_load_page())
        assert logotype_samokat.is_displayed()

    @allure.title('Проверить логотип "Самокат"')
    @allure.description('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката». после заполнение второй  части')
    def test_logotype_check_two(self, driver):
        order_page = OrderPage(driver)

        order_page.wait_for_load_page()
        order_page.click_button_order_down()
        order_page.fill_order_first_page()
        order_page.click_button_next()
        order_page.fill_order_second_page()

        logotype_samokat = order_page.check_logotype_samokat(order_page.wait_for_load_page())
        assert logotype_samokat.is_displayed()

    @allure.title('Проверить логотип "Яндекс"')
    @allure.description(
        'Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    def test_logotype_yandex(self, driver):
        order_page = OrderPage(driver)

        order_page.wait_for_load_page()
        order_page.click_button_order_down()
        order_page.click_logotype_yandex()

        assert "dzen.ru" in driver.current_url
