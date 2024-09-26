from stepik_final_test.pages.base_page import BasePage
from stepik_final_test.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_emtpy_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL), "Basket is not empty"

    def should_be_message_empty_basket(self):
        message_empty_basket = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text
        assert "Your basket is empty." in message_empty_basket, f"Expected message 'Your basket is empty'"