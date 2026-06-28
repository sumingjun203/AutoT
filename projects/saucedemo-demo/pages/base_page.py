"""
base_page.py - 所有 Page 的基类

封装 Selenium 常用操作，所有页面对象都继承此类。
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.logger import logger


class BasePage:
    """Page 基类"""

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10  # 默认等待超时

    def find_element(self, locator):
        """查找单个元素（显式等待）"""
        try:
            elem = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
            return elem
        except Exception as e:
            logger.error(f"元素未找到: {locator}, 错误: {e}")
            self.take_screenshot(f"element_not_found_{locator[1]}")
            raise

    def find_elements(self, locator):
        """查找多个元素"""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator):
        """点击元素"""
        elem = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        elem.click()
        logger.info(f"点击元素: {locator}")

    def input_text(self, locator, text):
        """输入文本（先清空）"""
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(text)
        logger.info(f"输入文本 '{text}' 到元素: {locator}")

    def get_text(self, locator):
        """获取元素文本"""
        return self.find_element(locator).text

    def get_attribute(self, locator, attr):
        """获取元素属性"""
        return self.find_element(locator).get_attribute(attr)

    def is_visible(self, locator):
        """判断元素是否可见"""
        try:
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def take_screenshot(self, name):
        """截图"""
        path = f"screenshots/{name}.png"
        self.driver.save_screenshot(path)
        logger.info(f"截图保存: {path}")
        return path

    def open_url(self, url):
        """打开 URL"""
        self.driver.get(url)
        logger.info(f"打开 URL: {url}")

    def get_title(self):
        """获取页面标题"""
        return self.driver.title