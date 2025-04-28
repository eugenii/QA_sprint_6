from pages.base_page import BasePage 
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):
    """Страница с формой заказа."""

    target = "https://qa-scooter.praktikum-services.ru/order"
    
    def click_to_order_button(
            self,
            locator,
            scroll=False):
        if scroll:
            self.scroll_to_element(locator)
        self.click_to_element(locator)
        return self.target in self.driver.current_url 
    
    def click_to_order_top(self):
        return self.click_to_order_button(
            locator=OrderPageLocators.BUTTON_TOP_LOCATOR,
            scroll=False
        )
    
    def click_to_order_bottom(self):
        return self.click_to_order_button(
            locator=OrderPageLocators.BUTTON_BOTTOM_LOCATOR,
            scroll=True
        )
    
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
        self.fill_field(
            locator=OrderPageLocators.METRO_FIELD_LOCATOR,
            value=params["metro"]
        )
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
        return True