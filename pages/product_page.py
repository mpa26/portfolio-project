from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket_page(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()
        # self.solve_quiz_and_get_code()
        # alert = self.browser.switch_to.alert
        # alert.accept()

    def should_check_product_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not present"
        assert self.is_element_present(*ProductPageLocators.ALERT_CART_STATUS), "No alert with cart status"
        alert_text = self.browser.find_element(*ProductPageLocators.ALERT_CART_STATUS).text.split()[-1]
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_cost == alert_text, \
            f"Product cost in cart is not equal to the product cost {alert_text} != {product_cost}"

    def should_be_present_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not present"
        assert self.is_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART), "No alert that a product has been added to cart"
        alert_text = self.browser.find_element(*ProductPageLocators.ALERT_ADDED_TO_CART).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # assert product_name in alert_text, \
        assert product_name == alert_text, \
            f"The alert contains wrong product name: {alert_text} - {product_name}"
