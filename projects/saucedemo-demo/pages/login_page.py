"""
login_page.py - 登录页 Page Object

对应 https://www.saucedemo.com/ 的登录页面
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    """登录页"""

    # 定位器
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    URL = "https://www.saucedemo.com/"

    def open(self):
        """打开登录页"""
        self.open_url(self.URL)
        return self

    def login(self, username, password):
        """
        执行登录操作
        :param username: 用户名
        :param password: 密码
        :return: 登录成功返回 InventoryPage，失败返回 self
        """
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

        # 简单判断：URL 变了就是成功
        if "inventory" in self.driver.current_url:
            return InventoryPage(self.driver)
        return self

    def get_error_message(self):
        """获取错误信息"""
        if self.is_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""