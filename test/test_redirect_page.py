import allure

from pages.redirect_page import RedirectPage


class TestRedirectPage:
    """Тестирование редиректов через логотип."""

    @allure.title('Проверка редиректа через логотип')
    @allure.description('Проверяем переход на главную.')
    def test_redirect_page(self, driver):
        """Проверяем, что клик на логотип *Самокат* со страницы заказа ведёт на главную."""
        redirect_page = RedirectPage(driver)
        assert redirect_page.click_to_logo() 

    @allure.title('Проверка редиректа через на Дзен')
    def test_redirect_dzen(self, driver):
        """Проверяем, что клик на логотип со страницы заказа ведет на Дзен"""
        redirect_page = RedirectPage(driver)
        assert redirect_page.click_to_yandex()