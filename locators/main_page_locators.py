from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для страницы авторизации."""

    QUESTION_LOCATOR = By.XPATH, "//div[@id='accordion__heading-{}']"
    ANSWER_LOCATOR = By.XPATH, "//div[@id='accordion__panel-{}']/p"
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, "//div[@id='accordion__heading-7']"
