import pytest

from pages.base_page import BasePage
from locators import *


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_load_page(self):
        return self.find_element(Element_check.MAIN_PAGE)

    def scroll_to_questions_block(self):
        self.scroll_to_element(Element_check.BLOCK_QUESTION)

    def get_question_element(self, question_text):
        locator = Element_check.check_question(question_text)
        return self.find_element(locator)

    def click_question(self, question_text):
        locator = Element_check.check_question(question_text)
        self.click_to_element(locator)

    def get_answer_element(self, answer_text):
        locator = Element_check.check_answer(answer_text)
        return self.is_element_visible(locator)

    def get_answer_text(self, answer_text):
        answer_element = self.get_answer_element(answer_text)
        return answer_element.text

    def is_question_visible(self, question_text):
        question_element = self.get_question_element(question_text)
        return question_element.is_displayed()

    def get_question_text(self, question_text):
        question_element = self.get_question_element(question_text)
        return question_element.text

    def check_question_visibility_and_text(self, question_text):
        question_element = self.get_question_element(question_text)
        return question_element.is_displayed()

