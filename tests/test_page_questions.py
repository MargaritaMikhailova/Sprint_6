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


    def check_answer_visibility_and_text(self, question_text, expected_answer):
        self.click_question(question_text)
        answer_element = self.get_answer_element(expected_answer)

        assert answer_element.is_displayed()
        assert expected_answer in answer_element.text


    @allure.title('Проверка, что вопросы есть на главной странице')
    @pytest.mark.parametrize("question,answer", Data.QA_DATA)
    def test_check_all_questions(self, driver, question, answer):

        main_page = MainPage(driver)
        main_page.wait_for_load_page()
        main_page.scroll_to_questions_block()


    def check_question_visibility_and_text(self, question_text):
        question_element = self.get_question_element(question_text)

        assert question_element.is_displayed()
        assert question_text in question_element.text





