import allure
import pytest

from data import personal_data
from pages.order_page import OrderPage


class TestOrderPage:
    """Testing order page."""

    @allure.title('Проверка перехода на страницу заказа')
    @allure.description('Переход с верхней кнопки.')
    def test_go_to_order_page_from_top(self, driver):
        """Go to order from top and bottom buttons."""
        
        order_page = OrderPage(driver)
        assert order_page.click_to_order_top()
    
    @allure.title('Проверка перехода на страницу заказа')
    @allure.description('Переход с нижней кнопки.')
    def test_go_to_order_page_from_bottom(self, driver):
        """Go to order from top and bottom buttons."""
        
        order_page = OrderPage(driver)
        assert order_page.click_to_order_bottom()

    @allure.title('Проверка выполнения заказа')
    @allure.description('Проводим два заказа и проверяем появление модального окна')
    @pytest.mark.parametrize(
            'num',
            [0, 1]
    )
    def test_fill_fields_1(self, driver, num):
        """Testing filling fields and continue button."""
        
        order_page = OrderPage(driver)
        assert order_page.fill_fields_1(personal_data[num])

