import pytest
from data import button_texts
from pages.main_page import MainPage


class TestMainPage:
    """Testin questions on main page."""
    
    @pytest.mark.parametrize(
            "num", 
            [
               0
            ]
            )
    def test_questions(self, driver, num):
        """Testin questions on main page."""
        main_page = MainPage(driver)
        main_page.click_to_question(num)
        assert main_page.get_answer_text(num) == button_texts[num][1]
          
