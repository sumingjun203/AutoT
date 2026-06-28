"""
auth_api.py - 鉴权相关 API
"""
from api.base_api import BaseAPI


class AuthAPI(BaseAPI):
    """鉴权模块 API"""

    def login(self, email, password):
        """登录获取 token"""
        payload = {"email": email, "password": password}
        return self.post("/login", json=payload)

    def register(self, email, password):
        """注册"""
        payload = {"email": email, "password": password}
        return self.post("/register", json=payload)