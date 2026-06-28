"""
test_user.py - 用户 API 测试
"""
import pytest
import allure

from utils.assertions import (
    assert_status_code,
    assert_json_key,
    assert_jsonpath,
)
from utils.read_yaml import get_test_data


@allure.feature("用户模块")
class TestUserAPI:
    """用户 API 测试类"""

    @allure.story("查询用户")
    @pytest.mark.smoke
    def test_list_users(self, user_api):
        """查询用户列表"""
        resp = user_api.list_users(page=1)

        with allure.step("断言状态码"):
            assert_status_code(resp, 200)

        with allure.step("断言返回数据"):
            data = resp.json()
            assert "data" in data
            assert len(data["data"]) > 0

    @allure.story("查询用户")
    def test_get_user_success(self, user_api):
        """获取单个用户 - 成功"""
        resp = user_api.get_user(2)

        assert_status_code(resp, 200)
        data = resp.json()
        assert "data" in data
        assert data["data"]["id"] == 2

    @allure.story("查询用户")
    def test_get_user_not_found(self, user_api):
        """获取不存在的用户"""
        resp = user_api.get_user_not_found(9999)

        assert_status_code(resp, 404)

    @allure.story("创建用户")
    @pytest.mark.parametrize("case", get_test_data("user", "create_cases"))
    def test_create_user_data_driven(self, user_api, case):
        """数据驱动：创建用户"""
        resp = user_api.create_user(case["name"], case["job"])

        assert_status_code(resp, 201)

        with allure.step("断言返回字段"):
            data = resp.json()
            assert data["name"] == case["name"]
            assert data["job"] == case["job"]
            assert "id" in data

    @allure.story("创建用户")
    def test_create_user_simple(self, user_api):
        """创建用户 - 简单版本"""
        resp = user_api.create_user("morpheus", "leader")

        assert_status_code(resp, 201)
        assert_json_key(resp, "name", "morpheus")
        assert_json_key(resp, "job", "leader")

    @allure.story("更新用户")
    def test_update_user(self, user_api):
        """更新用户"""
        resp = user_api.update_user(2, name="neo", job="the one")

        assert_status_code(resp, 200)
        data = resp.json()
        assert data["name"] == "neo"
        assert data["job"] == "the one"

    @allure.story("删除用户")
    def test_delete_user(self, user_api):
        """删除用户"""
        resp = user_api.delete_user(2)

        assert_status_code(resp, 204)

    @allure.story("鉴权")
    def test_create_user_with_token(self, authenticated_user_api):
        """带 token 创建用户"""
        resp = authenticated_user_api.create_user("Trinity", "hacker")

        assert_status_code(resp, 201)
        assert_json_key(resp, "name", "Trinity")