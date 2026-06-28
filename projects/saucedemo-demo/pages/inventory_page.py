"""
inventory_page.py - 商品列表页 Page Object
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.cart_page import CartPage


class InventoryPage(BasePage):
    """商品列表页"""

    # 定位器
    TITLE = (By.CSS_SELECTOR, ".title")
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")

    def get_title(self):
        """获取页面标题"""
        return self.get_text(self.TITLE)

    def get_inventory_count(self):
        """获取商品数量"""
        items = self.find_elements(self.INVENTORY_ITEMS)
        return len(items)

    def add_first_item_to_cart(self):
        """添加第一个商品到购物车"""
        first_add_btn = self.find_elements(self.ADD_TO_CART_BUTTON)[0]
        first_add_btn.click()

    def get_cart_badge_count(self):
        """获取购物车角标数量"""
        if self.is_visible(self.SHOPPING_CART_BADGE):
            return int(self.get_text(self.SHOPPING_CART_BADGE))
        return 0

    def sort_by(self, option_value):
        """
        排序
        :param option_value: 选项值（az/za/lohi/hilo）
        """
        from selenium.webdriver.support.ui import Select
        select = Select(self.find_element(self.SORT_DROPDOWN))
        select.select_by_value(option_value)

    def go_to_cart(self):
        """进入购物车"""
        self.click(self.SHOPPING_CART_LINK)
        return CartPage(self.driver)