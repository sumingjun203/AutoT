"""
test_login.py - 登录测试
"""
import pytest
import yaml


def load_login_data():
    """加载登录测试数据"""
    with open("data/login_data.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["login_cases"]


class TestLogin:
    """登录功能测试"""

    @pytest.mark.smoke
    def test_login_success(self, login_page):
        """登录成功"""
        result = login_page.login("standard_user", "secret_sauce")
        assert "inventory" in result.driver.current_url
        assert result.get_title() == "Products"

    @pytest.mark.parametrize("username,password,expected_error", [
        ("locked_out_user", "secret_sauce", "locked out"),
        ("invalid_user", "secret_sauce", "do not match"),
        ("standard_user", "wrong_password", "do not match"),
        ("", "", "required"),
    ])
    def test_login_failure(self, login_page, username, password, expected_error):
        """登录失败：多种异常场景"""
        result = login_page.login(username, password)
        error = result.get_error_message()
        assert expected_error.lower() in error.lower()

    def test_login_data_driven(self, login_page):
        """数据驱动：从 YAML 读取测试数据"""
        cases = load_login_data()
        for case in cases:
            result = login_page.login(case["username"], case["password"])
            if case["expect_success"]:
                assert "inventory" in result.driver.current_url
            else:
                assert result.get_error_message() != ""

    def test_login_logout_flow(self, login_page):
        """登录后退出再登录"""
        # 登录
        inventory = login_page.login("standard_user", "secret_sauce")
        assert "inventory" in inventory.driver.current_url

        # 退出（通过菜单）
        inventory.driver.find_element("id", "react-burger-menu-btn").click()
        import time
        time.sleep(1)
        inventory.driver.find_element("id", "logout_sidebar_link").click()

        # 重新登录
        login_page_new = LoginPage(inventory.driver)
        assert "saucedemo" in inventory.driver.current_url