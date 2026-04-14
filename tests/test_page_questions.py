import pytest
import allure

from data import Data
from pages.main_page_question import MainPage


class TestPageQuestion:

    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном»')
    @pytest.mark.parametrize("question,answer", Data.QA_DATA)
    def test_page(self, driver, question, answer):

        main_page = MainPage(driver)
        main_page.wait_for_load_page()
        main_page.scroll_to_questions_block()
        main_page.click_question(question)

        answer_text = main_page.get_answer_text(answer)
        assert answer in answer_text


    @allure.title('Проверка, что вопросы есть на главной странице')
    @pytest.mark.parametrize("question,answer", Data.QA_DATA)
    def test_check_all_questions(self, driver, question, answer):

        main_page = MainPage(driver)
        main_page.wait_for_load_page()
        main_page.scroll_to_questions_block()

        assert main_page.is_question_visible(question)
        question_text = main_page.get_question_text(question)
        assert question in question_text







