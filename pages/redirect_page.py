import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.redirect_locators import RedirectLocators


class RedirectPage(BasePage):
    """Переходы на главную и редирект на Дзен."""

    from_page = "https://qa-scooter.praktikum-services.ru/order"
    target = "https://qa-scooter.praktikum-services.ru/"
    target_yandex = "https://dzen.ru/?yredirect"

    @allure.step("Нажать на логотип и проверить редирект на главную страницу.")
    def click_to_logo(self):
        """Нажать на логотип и проверить редирект на главную страницу."""

        self.driver.get(self.from_page)

        WebDriverWait(self.driver, 15).until(EC.url_to_be(self.from_page))

        self.click_to_element(RedirectLocators.SCOOTER_LOGO_LOCATOR)

        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.target))

        return "qa-scooter.praktikum-services.ru" in self.driver.current_url

    @allure.step("Нажать на логотип и проверить редирект на Дзен.")
    def click_to_yandex(self):
        """Нажать на логотип и проверить редирект на Дзен."""

        self.click_to_element(RedirectLocators.YANDEX_REDIRECT_LOCATOR)

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        all_windows = self.driver.window_handles

        self.driver.switch_to.window(all_windows[-1])

        WebDriverWait(self.driver, 10).until(EC.url_contains("https://dzen.ru/?yredirect"))

        return self.target_yandex in self.driver.current_url
