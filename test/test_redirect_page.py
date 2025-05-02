import allure

from pages.redirect_page import RedirectPage


@allure.title('Проверка редиректов через логотипы')
@allure.description('Проверяем переход на главную и на страницу Дзен.')
class TestRedirectPage:
    """Тестирование редиректов через логотип."""

    def test_redirect_page(self, driver):
        """Проверяем, что клик на логотип *Самокат* со страницы заказа ведёт на главную."""
        redirect_page = RedirectPage(driver)
        assert redirect_page.click_to_logo() 

    def test_redirect_dzen(self, driver):
        """Проверяем, что клик на логотип со страницы заказа ведет на Дзен"""
        redirect_page = RedirectPage(driver)
        assert redirect_page.click_to_yandex()