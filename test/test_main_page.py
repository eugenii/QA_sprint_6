import allure
import pytest
from data import button_texts
from pages.main_page import MainPage


class TestMainPage:
    """Testin questions on main page."""
    
    @allure.title('Проверка текстов ответов на Основные вопросы')
    @allure.description('На главной странице прокручиваем вниз и проверяем вопросы по очереди')
    @pytest.mark.parametrize(
        "num", 
        [
            0, 1, 2, 3, 4, 5, 6, 7
        ]
    )
    def test_questions(self, driver, num):
        """Testin questions on main page."""

        main_page = MainPage(driver)
        main_page.click_to_question(num)
        assert main_page.get_answer_text(num) == button_texts[num][1]
