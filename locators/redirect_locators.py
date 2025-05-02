from selenium.webdriver.common.by import By


class RedirectLocators:
    """Локаторы для переходов."""
    
    SCOOTER_LOGO_LOCATOR = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_REDIRECT_LOCATOR = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    CLOSE_BANNER_LOCATOR = (By.XPATH, "//div[contains(@class, 'yf70fb875')]//span[@aria-label='Закрыть']")
