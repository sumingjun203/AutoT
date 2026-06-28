"""
test_auth.py - 鉴权 API 测试
"""
import pytest
import allure

from utils.assertions import assert_status_code, assert_json_key
from utils.read_yaml import get_test_data


@allure.feature("鉴权模块")
class TestAuthAPI:
    """鉴权 API 测试"""

    @allure.story("登录")
    @pytest.mark.smoke
    def test_login_success(self, auth_api):
        """登录成功"""
        resp = auth_api.login("eve.holt@reqres.in", "cityslicka")

        assert_status_code(resp, 200)
        assert_json_key(resp, "token")

    @allure.story("登录")
    @pytest.mark.parametrize("case", get_test_data("auth", "login_failure_cases"))
    def test_login_failure(self, auth_api, case):
        """登录失败 - 参数化"""
        resp = auth_api.login(case["email"], case["password"])

        assert_status_code(resp, 400)
        assert_json_key(resp, "error", case["expected_error"])

    @allure.story("注册")
    def test_register_success(self, auth_api):
        """注册成功"""
        resp = auth_api.register("eve.holt@reqres.in", "pistol")

        assert_status_code(resp, 200)
        assert_json_key(resp, "token")
        assert_json_key(resp, "id")