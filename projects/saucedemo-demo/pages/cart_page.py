"""
cart_page.py - 购物车页 Page Object
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    """购物车页"""

    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "[data-test^='remove']")

    def get_cart_items_count(self):
        """获取购物车商品数量"""
        return len(self.find_elements(self.CART_ITEMS))

    def click_checkout(self):
        """点击结算"""
        self.click(self.CHECKOUT_BUTTON)
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)

    def remove_first_item(self):
        """移除第一个商品"""
        remove_btns = self.find_elements(self.REMOVE_BUTTON)
        if remove_btns:
            remove_btns[0].click()