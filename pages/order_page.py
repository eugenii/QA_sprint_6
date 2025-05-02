import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage 
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    """Страница с формой заказа."""

    target = "https://qa-scooter.praktikum-services.ru/order"
    
    @allure.step("Кликнуть на кнопку заказа.")
    def click_to_order_button(
            self,
            locator,
            scroll=False):
        if scroll:
            self.scroll_to_element(locator)
        self.click_to_element(locator)
        return self.target in self.driver.current_url 
    
    @allure.step("Кликнуть на кнопку заказа сверху.")
    def click_to_order_top(self):
        return self.click_to_order_button(
            locator=OrderPageLocators.BUTTON_TOP_LOCATOR,
            scroll=False
        )
    
    @allure.step("Кликнуть на кнопку заказа снизу.")
    def click_to_order_bottom(self):
        return self.click_to_order_button(
            locator=OrderPageLocators.BUTTON_BOTTOM_LOCATOR,
            scroll=True
        )
    
    @allure.step("Заполнить поля формы.")
    def fill_fields_1(self, params):
        self.driver.get(self.target)
        self.fill_field(
            locator=OrderPageLocators.NAME_FIELD_LOCATOR,
            value=params["name"]
        )
        self.fill_field(
            locator=OrderPageLocators.SURNAME_FIELD_LOCATOR,
            value=params["surname"]
        )
        self.fill_field(
            locator=OrderPageLocators.ADRESS_FIELD_LOCATOR,
            value=params["adress"]
        )
        self.click_to_element(OrderPageLocators.METRO_FIELD_LOCATOR)
        self.fill_field(
            locator=OrderPageLocators.METRO_FIELD_LOCATOR,
            value=params["metro"]
        )
        f_locator = self.format_locators(OrderPageLocators.METRO_SCROL_LOCATOR, params["metro"])
        x = self.find_element_with_wait(f_locator)
        x.click()
        self.fill_field(
            locator=OrderPageLocators.PHONE_FIELD_LOCATOR,
            value=params["phone"]
        )
        # Ожидаем появления баннера и закрываем его
        WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(OrderPageLocators.CLOSE_COOKIE_BANNER_LOCATOR)
        ).click()
        print("Cookie banner closed.")
        self.click_to_element(OrderPageLocators.FORWARD_BUTTON_LOCATOR)
        WebDriverWait(self.driver, timeout=10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_HEADER_2_LOCATOR)
        )
        print("Order header 2 visible.")

        self.click_to_element(OrderPageLocators.DATE_FIELD_LOCATOR)

        self.fill_field(
            locator=OrderPageLocators.DATE_FIELD_LOCATOR,
            value=params["date"]
        )
        self.click_to_element(OrderPageLocators.ORDER_HEADER_2_LOCATOR)

        self.click_to_element(OrderPageLocators.DUR_FIELD_LOCATOR)

        duration_locator = self.format_locators(OrderPageLocators.DUR_FIELD_DAYS_LOCATOR, params["duration"])  # (By.XPATH, f"//div[@class='Dropdown-option' and text()='{params['duration']}']")
        duration = self.find_element_with_wait(duration_locator)

        duration.click()
        print("Duration selected.")
        scooter_color = self.find_element_with_wait(OrderPageLocators.SCOOTER_BLACK_COLOR_LOCATOR)
        scooter_color.click()

        self.fill_field(
            locator=OrderPageLocators.COMMENT_FIELD_LOCATOR,
            value=params["comment"]
        )

        order = self.find_element_with_wait(OrderPageLocators.ORDER_BUTTON_LOCATOR)
        order.click()
        yes = self.find_element_with_wait(OrderPageLocators.ACCEPT_ORDER_BUTTON_LOCATOR)
        yes.click()

        status = self.find_element_with_wait(OrderPageLocators.STATUS_OK_LOCATOR)

        return  "Заказ оформлен" in status.text
