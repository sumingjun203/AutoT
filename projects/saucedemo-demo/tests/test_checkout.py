"""
test_checkout.py - 结算测试
"""
import pytest


class TestCheckout:
    """结算流程测试"""

    def test_checkout_flow_success(self, logged_in_page):
        """完整结算流程"""
        logged_in_page.add_first_item_to_cart()
        cart = logged_in_page.go_to_cart()

        checkout = cart.click_checkout()
        checkout.fill_info("John", "Doe", "12345")

        # 应该跳转到 step two
        assert "checkout-step-two" in checkout.driver.current_url

        total = checkout.get_total()
        assert "Total:" in total

    def test_checkout_missing_info(self, logged_in_page):
        """缺少必填信息"""
        logged_in_page.add_first_item_to_cart()
        cart = logged_in_page.go_to_cart()

        checkout = cart.click_checkout()
        checkout.fill_info("", "", "")

        error = checkout.get_error()
        assert "required" in error.lower() or "First Name is required" in error

    def test_checkout_complete(self, logged_in_page):
        """完成订单"""
        logged_in_page.add_first_item_to_cart()
        cart = logged_in_page.go_to_cart()

        checkout = cart.click_checkout()
        checkout.fill_info("John", "Doe", "12345")
        checkout.finish()

        message = checkout.get_complete_message()
        assert "THANK YOU" in message.upper()