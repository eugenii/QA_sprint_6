from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы для страницы заказа."""
    
    # Локаторы кнопки заказа на главной
    BUTTON_TOP_LOCATOR = By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button')]"
    BUTTON_BOTTOM_LOCATOR = By.XPATH, "//div[contains(@class, 'Home')]/button[contains(@class, 'Button_Button')]"
    BUTTON_LOCATOR_TO_SCROLL = By.XPATH, "//div[contains(@class, 'Home')]/button[contains(@class, 'Button_Button')]"

    # Локаторы полей заказа
    NAME_FIELD_LOCATOR = By.XPATH, "//input[contains(@placeholder, '* Имя')]"
    SURNAME_FIELD_LOCATOR = By.XPATH, "//input[contains(@placeholder, '* Фамилия')]"
    ADRESS_FIELD_LOCATOR = By.XPATH, "//input[contains(@placeholder, '* Адрес')]"
    METRO_FIELD_LOCATOR = By.XPATH, "//input[contains(@placeholder, '* Станция метро')]"
    PHONE_FIELD_LOCATOR = By.XPATH, "//input[contains(@placeholder, '* Телефон')]"
    DATE_FIELD_LOCATOR = By.XPATH, "//input[contains(@placeholder, '* Когда привезти')]"
    DUR_FIELD_LOCATOR = By.XPATH, "//input[contains(@placeholder, '* Срок аренды')]"
    COMMENT_FIELD_LOCATOR = By.XPATH, "//input[contains(@placeholder, '* Комментарий')]"

    FORWARD_BUTTON_LOCATOR = By.XPATH, "//button[text()='Далее']"
    ORDER_BUTTON_LOCATOR = By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"

    ORDER_HEADER_1_LOCATOR = By.XPATH, "//div[contains(@class,'Order_Header') and text()='Для кого самокат']"
    ORDER_HEADER_2_LOCATOR = By.XPATH, "//div[contains(@class,'Order_Header') and text()='Про аренду']"

    # Локатор для кнопки "Закрыть" в баннере
    CLOSE_COOKIE_BANNER_LOCATOR = (By.XPATH, "//button[contains(text(), 'да все привыкли')]")
       