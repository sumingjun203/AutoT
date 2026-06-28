"""
conftest.py - 共享 fixture

为 API 测试提供：
- API 实例
- 已登录的 session（带 token）
- 测试数据加载
"""
import pytest

from api.auth_api import AuthAPI
from api.user_api import UserAPI
from utils.config import BASE_URL
from utils.logger import logger


@pytest.fixture
def user_api():
    """用户 API 实例"""
    return UserAPI()


@pytest.fixture
def auth_api():
    """鉴权 API 实例"""
    return AuthAPI()


@pytest.fixture
def authenticated_user_api():
    """已登录的用户 API（带 token）"""
    auth = AuthAPI()
    resp = auth.login("eve.holt@reqres.in", "cityslicka")
    assert resp.status_code == 200, f"登录失败: {resp.text}"
    token = resp.json().get("token")
    assert token, "登录响应中没有 token"

    api = UserAPI()
    api.set_token(token)
    logger.info(f"已登录，token 长度: {len(token)}")
    return api


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL