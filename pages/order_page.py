from pages.base_page import BasePage 
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
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
        self.click_to_element(OrderPageLocators.METRO_FIELD_LOCATOR)
        # sleep(1)
        self.fill_field(
            locator=OrderPageLocators.METRO_FIELD_LOCATOR,
            value=params["metro"]
        )
        # sleep(3)
        # Бляха-муха, всю душу вынули....
        x=self.find_element_with_wait(OrderPageLocators.METRO_SCROL_LOCATOR)
        # sleep(3)
        x.click()
        # sleep(1)
        self.fill_field(
            locator=OrderPageLocators.PHONE_FIELD_LOCATOR,
            value=params["phone"]
        )
        sleep(3)
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
        # Нажимаем на кнопку "Далее"
        self.click_to_element(OrderPageLocators.DATE_FIELD_LOCATOR)
        sleep(1)
        self.fill_field(
            locator=OrderPageLocators.DATE_FIELD_LOCATOR,
            value=params["date"]
        )
        self.click_to_element(OrderPageLocators.ORDER_HEADER_2_LOCATOR)
        sleep(1)
        self.click_to_element(OrderPageLocators.DUR_FIELD_LOCATOR)
        sleep(1)
        # self.fill_field(
        #     locator=OrderPageLocators.DUR_FIELD_LOCATOR,
        #     value=params["duration"]
        # )
        duration = self.find_element_with_wait(OrderPageLocators.DUR_FIELD_DAYS_LOCATOR)  # [1].format(params["duration"])
        print(duration)
        sleep(5)
        # self.find_element_with_wait(duration)
        duration.click()
        print("Duration selected.")
        scooter_color = self.find_element_with_wait(OrderPageLocators.SCOOTER_BLACK_COLOR_LOCATOR)
        scooter_color.click()
        sleep(1)
        self.fill_field(
            locator=OrderPageLocators.COMMENT_FIELD_LOCATOR,
            value=params["comment"]
        )
        sleep(5)
        order = self.find_element_with_wait(OrderPageLocators.ORDER_BUTTON_LOCATOR)
        order.click()
        yes = self.find_element_with_wait(OrderPageLocators.ACCEPT_ORDER_BUTTON_LOCATOR)
        yes.click()
        sleep(5)
        status = self.find_element_with_wait(OrderPageLocators.STATUS_OK_LOCATOR)
        # status.click()
        return   "Заказ оформлен" in status.text