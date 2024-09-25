from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import ProductPageLocator

class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocator.ADD_TO_BASKET), "Button is not presented"
        button_add = self.browser.find_element(*ProductPageLocator.ADD_TO_BASKET)
        button_add.click()
    def should_be_messages(self):
        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located(ProductPageLocator.MESSAGE_ADD_TO_BASKET)
        )
        product_name = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductPageLocator.MESSAGE_PRODUCT_NAME).text
        price = self.browser.find_element(*ProductPageLocator.PRICE).text
        message_price = self.browser.find_element(*ProductPageLocator.MESSAGE_PRICE).text
        assert self.is_element_present(*ProductPageLocator.MESSAGE_ADD_TO_BASKET), "Message not found"
        assert product_name in message_product_name, f"Expected '{product_name}' to be in message: '{message_product_name}'"
        assert price in message_price, f"Expected '{price}' to be in message: '{message_price}'"