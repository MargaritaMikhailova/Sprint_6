from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.long_wait = WebDriverWait(driver, 30)

    def wait_for_load_page(self):
        return self.wait.until(EC.visibility_of_element_located(Element_check.MAIN_PAGE))

    def scroll_to_questions_block(self):
        block_item = self.wait.until(EC.visibility_of_element_located(Element_check.BLOCK_QUESTION))
        self.driver.execute_script("arguments[0].scrollIntoView();", block_item)
        return block_item

    def get_question_element(self, question_text):
        locator = Element_check.check_question(question_text)
        return self.long_wait.until(EC.visibility_of_element_located(locator))

    def click_question(self, question_text):
        question_element = self.get_question_element(question_text)
        self.driver.execute_script("arguments[0].click();", question_element)
        return question_element

    def get_answer_element(self, answer_text):
        locator = Element_check.check_answer(answer_text)
        return self.long_wait.until(EC.visibility_of_element_located(locator))

    def get_answer_text(self, answer_text):
        answer_element = self.get_answer_element(answer_text)
        return answer_element.text

    def is_question_visible(self, question_text):
        question_element = self.get_question_element(question_text)
        return question_element.is_displayed()

    def get_question_text(self, question_text):
        question_element = self.get_question_element(question_text)
        return question_element.text
