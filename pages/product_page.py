from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_basket_page(self):
        login_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        login_link.click()
        # alert = self.browser.switch_to.alert
        # alert.accept()

    def should_be_product_status(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_STATUS), "Fail. Product status is wrong"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Fail. Product name is wrong"
        # class="alertinner"
        # <strong> The shellcoder's handbook

    def should_be_product_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST), "Fail. Product cost is wrong"
