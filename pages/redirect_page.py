import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.redirect_locators import RedirectLocators

from data import URLS


class RedirectPage(BasePage):
    """Переходы на главную и редирект на Дзен."""

    from_page = URLS.ORDER_PAGE
    target = URLS.MAIN_PAGE
    target_yandex = URLS.DZEN_PAGE

    @allure.step("Нажать на логотип и проверить редирект на главную страницу.")
    def click_to_logo(self):
        """Нажать на логотип и проверить редирект на главную страницу."""

        return self.redirect(self.target, RedirectLocators.SCOOTER_LOGO_LOCATOR, change_url=URLS.ORDER_PAGE, change_window=False)
        

    @allure.step("Нажать на логотип и проверить редирект на Дзен.")
    def click_to_yandex(self):
        """Нажать на логотип и проверить редирект на Дзен."""

        return self.redirect(self.target_yandex, RedirectLocators.YANDEX_REDIRECT_LOCATOR, change_url=None, change_window=True)
