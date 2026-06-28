"""
user_api.py - 用户相关 API
"""
from api.base_api import BaseAPI


class UserAPI(BaseAPI):
    """用户模块 API"""

    def list_users(self, page=1):
        """获取用户列表"""
        return self.get("/users", params={"page": page})

    def get_user(self, user_id):
        """获取单个用户"""
        return self.get(f"/users/{user_id}")

    def get_user_not_found(self, user_id):
        """用户不存在（测试 404）"""
        return self.get(f"/users/{user_id}")

    def create_user(self, name, job):
        """创建用户"""
        payload = {"name": name, "job": job}
        return self.post("/users", json=payload)

    def update_user(self, user_id, name=None, job=None):
        """更新用户（PUT 全量）"""
        payload = {"name": name, "job": job}
        return self.put(f"/users/{user_id}", json=payload)

    def delete_user(self, user_id):
        """删除用户"""
        return self.delete(f"/users/{user_id}")