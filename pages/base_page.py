import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.long_wait = WebDriverWait(driver, 30)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click(self, locator, timeout=10):
        element = self.find_clickable_element(locator, timeout)
        element.click()

    def click_with_scroll(self, locator, timeout=10):
        element = self.find_clickable_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator, text, timeout=10):
        element = self.find_clickable_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        return self.find_element(locator, timeout).text

    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def scroll_to_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def wait_for_url_contains(self, url_part, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))

    def switch_to_new_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])