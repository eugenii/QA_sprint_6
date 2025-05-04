from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    """Base methods for all pages."""
    
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, timeout=20).until(
            expected_conditions.visibility_of_element_located(locator)
            )
        
        return self.driver.find_element(*locator)
    
    def click_to_element(self, locator):
        WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.element_to_be_clickable(locator)
            )
        self.find_element_with_wait(locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        
        return self.find_element_with_wait(locator).text
    
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        
        return method, locator.format(num)
    
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_with_scroll(self, locator, target, scroll=False):
        if scroll:
            self.scroll_to_element(locator)
        self.click_to_element(locator)
        return target in self.driver.current_url 

    def wait_for_page_load(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout=timeout).until(
            expected_conditions.visibility_of_element_located(locator)
            )
        
    def fill_field(self, locator, value):
        field = self.find_element_with_wait(locator)
        field.clear()
        field.send_keys(value)

    def redirect(self, url, locator, change_url=None, change_window=False):
        if change_url:
            self.driver.get(change_url)
            WebDriverWait(self.driver, timeout=10).until(
                expected_conditions.url_to_be(change_url)
                )
            self.click_to_element(locator)
        if change_window:
            self.click_to_element(locator)
            WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
            all_windows = self.driver.window_handles
            self.driver.switch_to.window(all_windows[-1])
        
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))

        return url in self.driver.current_url

    # def close_banner(self, locator):
    #             # Ожидаем появления баннера и закрываем его
    #     WebDriverWait(self.driver, timeout=10).until(
    #         EC.element_to_be_clickable(OrderPageLocators.CLOSE_COOKIE_BANNER_LOCATOR)
    #     ).click()
    #     self.click_to_element(OrderPageLocators.FORWARD_BUTTON_LOCATOR)
    #     WebDriverWait(self.driver, timeout=10).until(
    #         EC.visibility_of_element_located(OrderPageLocators.ORDER_HEADER_2_LOCATOR)
    #     )