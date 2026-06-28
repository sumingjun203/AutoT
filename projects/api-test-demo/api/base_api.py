"""
base_api.py - 所有 API 的基类

封装 HTTP 请求、Session、Header 等公共逻辑。
"""
import json
from functools import wraps

import allure
import requests

from utils.config import BASE_URL, TIMEOUT
from utils.logger import logger


def allure_attach_response(func):
    """装饰器：自动把响应附加到 Allure 报告"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        resp = func(self, *args, **kwargs)
        try:
            allure.attach(
                json.dumps(resp.json(), indent=2, ensure_ascii=False),
                name=f"Response: {resp.request.method} {resp.url}",
                attachment_type=allure.attachment_type.JSON,
            )
        except Exception:
            pass
        return resp
    return wrapper


class BaseAPI:
    """所有 API 的基类"""

    def __init__(self, base_url=None):
        self.base_url = base_url or BASE_URL
        self.session = requests.Session()
        self.timeout = TIMEOUT
        self.token = None

    def _headers(self):
        """默认 Header"""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-api-key": "reqres-free-v1",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    @allure_attach_response
    def _request(self, method, endpoint, **kwargs):
        """统一请求方法"""
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("timeout", self.timeout)
        kwargs.setdefault("headers", self._headers())

        logger.info(f"[{method}] {url}")
        logger.debug(f"请求参数: {kwargs}")

        resp = self.session.request(method, url, **kwargs)
        logger.info(f"响应状态: {resp.status_code}")
        return resp

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)

    def set_token(self, token):
        """设置鉴权 token"""
        self.token = token
        logger.info(f"Token 已设置")