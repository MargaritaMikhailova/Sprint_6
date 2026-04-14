import pytest
import allure

from pages.main_page_logotype import LogotypePage
from data import ButtonData

class TestLogo:

    @allure.title('Проверить логотип "Самокат"')
    @allure.description('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката». после заполение первой части')
    @pytest.mark.parametrize("button_method, button_name", ButtonData.BUTTON_PARAMS)
    def test_logotype_check_one(self, driver, button_method, button_name):
        logotype_page = LogotypePage(driver)

        logotype_page.wait_for_load_page()
        getattr(logotype_page, button_method)()
        logotype_page.fill_order_first_page()

        logotype_samokat = logotype_page.check_logotype_samokat()
        assert logotype_samokat.is_displayed()

    @allure.title('Проверить логотип "Самокат"')
    @allure.description('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката». после заполнение второй  части')
    @pytest.mark.parametrize("button_method, button_name", ButtonData.BUTTON_PARAMS)
    def test_logotype_check_two(self, driver, button_method, button_name):
        logotype_page = LogotypePage(driver)

        logotype_page.wait_for_load_page()
        getattr(logotype_page, button_method)()
        logotype_page.fill_order_first_page()
        logotype_page.click_button_next()
        logotype_page.fill_order_second_page()

        logotype_samokat = logotype_page.check_logotype_samokat()
        assert logotype_samokat.is_displayed()

    @allure.title('Проверить логотип "Яндекс"')
    @allure.description(
        'Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    def test_logotype_yandex(self, driver):
        logotype_page = LogotypePage(driver)

        logotype_page.wait_for_load_page()
        logotype_page.click_button_order_down()

        logotype_samokat = logotype_page.click_logotype_yandex()
        assert logotype_samokat is True
