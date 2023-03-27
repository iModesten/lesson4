from .base_page import BasePage
from .locators import ProductPageLocators
from .base_page import solve_quiz_and_get_code
import time

class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()
        solve_quiz_and_get_code(self)
        time.sleep(1)

    def should_be_message_about_adding_a_product(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Message about adding a product is absent"

    def should_be_same_product_name_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text, "Product name doesn't match product price in the message"

    def shoulbe_be_message_about_product_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_PRICE), "Message about product proce is absent"

    def should_be_same_product_price_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_MESSSAGE).text, "Product price doesn't match the product price in the message"
