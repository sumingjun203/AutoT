"""
checkout_page.py - 结算页 Page Object
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """结算页"""

    # 第一步：填写信息
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    # 第二步：确认订单
    FINISH_BUTTON = (By.ID, "finish")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    # 第三步：完成
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")

    def fill_info(self, first_name, last_name, postal_code):
        """填写订单信息"""
        self.input_text(self.FIRST_NAME, first_name)
        self.input_text(self.LAST_NAME, last_name)
        self.input_text(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def get_error(self):
        """获取错误信息"""
        if self.is_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""

    def get_total(self):
        """获取总价"""
        return self.get_text(self.TOTAL_LABEL)

    def finish(self):
        """完成订单"""
        self.click(self.FINISH_BUTTON)

    def get_complete_message(self):
        """获取完成信息"""
        return self.get_text(self.COMPLETE_HEADER)