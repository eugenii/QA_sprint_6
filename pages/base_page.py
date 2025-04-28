import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import button_texts


class BasePage:
    """Base methods for all pages."""
    
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, timeout=20).until(
            expected_conditions.visibility_of_element_located(locator)
            )
        return self.driver.find_element(*locator)
    
    def click_to_element(self, locator):
        WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.element_to_be_clickable(locator)
            )
        self.find_element_with_wait(locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
    
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        return method, locator.format(num)
    
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_page_load(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout=timeout).until(
            expected_conditions.visibility_of_element_located(locator)
            )
        
    def fill_field(self, locator, value):
        field = self.find_element_with_wait(locator)
        field.clear()
        field.send_keys(value)