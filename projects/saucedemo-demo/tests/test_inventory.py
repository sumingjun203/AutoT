"""
test_inventory.py - 商品列表测试
"""
import pytest


class TestInventory:
    """商品列表功能测试"""

    def test_inventory_page_load(self, logged_in_page):
        """商品页正常加载"""
        assert logged_in_page.get_title() == "Products"
        assert logged_in_page.get_inventory_count() == 6

    def test_sort_by_name_az(self, logged_in_page):
        """按名称 A-Z 排序"""
        logged_in_page.sort_by("az")
        # 第一个商品名称首字母应该是 A 附近
        items = logged_in_page.driver.find_elements("css selector", ".inventory_item_name")
        first_name = items[0].text
        assert first_name.startswith(("Sauce Labs Backpack", "Sauce Labs Bike"))

    def test_sort_by_price_low_to_high(self, logged_in_page):
        """按价格从低到高排序"""
        logged_in_page.sort_by("lohi")
        items = logged_in_page.driver.find_elements("css selector", ".inventory_item_price")
        prices = [float(item.text.replace("$", "")) for item in items]
        assert prices == sorted(prices)

    def test_add_to_cart(self, logged_in_page):
        """添加商品到购物车"""
        logged_in_page.add_first_item_to_cart()
        assert logged_in_page.get_cart_badge_count() == 1