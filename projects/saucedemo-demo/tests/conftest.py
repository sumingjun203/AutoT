"""
conftest.py - 共享 fixture

为所有测试文件提供：
- driver fixture（Selenium WebDriver）
- 自动截图
- 自动登录（可选）
"""
import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from utils.logger import logger


@pytest.fixture(scope="function")
def driver():
    """
    提供 WebDriver 实例
    - 默认 Chrome 无头模式
    - 每个测试结束后自动 quit
    """
    chrome_options = Options()

    # 无头模式（CI 环境）
    if os.getenv("HEADLESS", "true").lower() == "true":
        chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.fixture
def login_page(driver):
    """提供登录页实例"""
    return LoginPage(driver).open()


@pytest.fixture
def logged_in_page(driver):
    """已登录的 InventoryPage"""
    login_page = LoginPage(driver).open()
    return login_page.login("standard_user", "secret_sauce")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    自动截图：测试失败时保存截图到 screenshots/
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.nodeid.replace("/", "_").replace("::", "__")
            path = f"screenshots/FAILED_{test_name}_{timestamp}.png"
            driver.save_screenshot(path)
            logger.error(f"测试失败，截图保存: {path}")