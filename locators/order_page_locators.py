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
    METRO_FIELD_LOCATOR = By.XPATH, "//div[@class='select-search__value']/input[contains(@placeholder, '* Станция метро')]" # and @class='select-search__input']" 
    METRO_SCROL_LOCATOR = By.XPATH, "//div[contains(@class, 'Order_Text') and text()='Сокольники']"   
    PHONE_FIELD_LOCATOR = By.XPATH, "//input[contains(@placeholder, '* Телефон')]"
    DATE_FIELD_LOCATOR = By.XPATH, "//input[contains(@placeholder, '* Когда привезти')]"
    DUR_FIELD_LOCATOR = By.XPATH, "//div[contains(@class, 'Dropdown-placeholder')]"
    DUR_FIELD_DAYS_LOCATOR = By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"
    SCOOTER_BLACK_COLOR_LOCATOR = By.XPATH, "//input[@id='black']"
    SCOOTER_GREY_COLOR_LOCATOR = By.XPATH, "//input[@id='grey']"
    COMMENT_FIELD_LOCATOR = By.XPATH, "//input[contains(@placeholder, 'Комментарий')]"
    
    # Кнопки Далее и Заказать (окончание)
    FORWARD_BUTTON_LOCATOR = By.XPATH, "//button[text()='Далее']"
    ORDER_BUTTON_LOCATOR = By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"

    ORDER_HEADER_1_LOCATOR = By.XPATH, "//div[contains(@class,'Order_Header') and text()='Для кого самокат']"
    ORDER_HEADER_2_LOCATOR = By.XPATH, "//div[contains(@class,'Order_Header') and text()='Про аренду']"

    # Финал заказа.
    ACCEPT_ORDER_BUTTON_LOCATOR = By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Да']"   
    STATUS_OK_LOCATOR = By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']"
    # Локатор для кнопки "Закрыть" в баннере
    CLOSE_COOKIE_BANNER_LOCATOR = (By.XPATH, "//button[contains(text(), 'да все привыкли')]")


# Локатор для элемента выпадающего списка. Море крови, км нервов..
# //div[contains(@class, 'Order_Text') and normalize-space(text())='Чистые пруды']
