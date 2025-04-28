import pytest
from data import button_texts, personal_data
from pages.order_page import OrderPage


class TestOrderPage:
    """Testing order page."""

    def test_go_to_order_page_from_top(self, driver):
        """Go to order from top and bottom buttons."""
        order_page = OrderPage(driver)
        assert order_page.click_to_order_top()
    
    def test_go_to_order_page_from_bottom(self, driver):
        """Go to order from top and bottom buttons."""
        order_page = OrderPage(driver)
        assert order_page.click_to_order_bottom()

    def test_fill_fields_1(self, driver):
        """Testing filling fields and continue button."""
        order_page = OrderPage(driver)
        
        assert order_page.fill_fields_1(personal_data[0])

