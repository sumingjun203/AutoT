"""
test_cart.py - 购物车测试
"""
import pytest


class TestCart:
    """购物车功能测试"""

    def test_add_item_to_cart(self, logged_in_page):
        """添加商品到购物车"""
        logged_in_page.add_first_item_to_cart()
        cart = logged_in_page.go_to_cart()
        assert cart.get_cart_items_count() == 1

    def test_remove_item_from_cart(self, logged_in_page):
        """从购物车移除商品"""
        logged_in_page.add_first_item_to_cart()
        cart = logged_in_page.go_to_cart()
        assert cart.get_cart_items_count() == 1

        cart.remove_first_item()
        assert cart.get_cart_items_count() == 0

    def test_continue_shopping(self, logged_in_page):
        """继续购物按钮返回商品列表"""
        logged_in_page.add_first_item_to_cart()
        cart = logged_in_page.go_to_cart()

        cart.driver.find_element("id", "continue-shopping").click()
        assert "inventory" in cart.driver.current_url