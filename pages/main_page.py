from pages.base_page import BasePage 
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    """Стартовая страница с ответами на вопросы."""


    def click_to_question(self, num):
        """Передали номер вопроса."""
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        print(locator_q_formatted)
        self.click_to_element(locator_q_formatted)


    def get_answer_text(self, num):
        """Передали номер вопроса."""
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_a_formatted)
    
    def get_question_text(self, num):
        """Передали номер вопроса."""
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        print(locator_q_formatted)
        return self.get_text_from_element(locator_q_formatted)