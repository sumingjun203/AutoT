"""
conftest.py - 共享 fixture

为所有测试文件提供共享的 fixture。
"""
import pytest

from src.calculator import Calculator


@pytest.fixture
def calc():
    """function 级 fixture：每个测试都获得一个新实例"""
    return Calculator()


@pytest.fixture(scope="module")
def calc_module():
    """module 级 fixture：整个测试文件共享一个实例"""
    return Calculator()


@pytest.fixture(scope="session")
def config():
    """session 级 fixture：整个测试会话共享的配置"""
    return {
        "tolerance": 0.0001,  # 浮点数比较精度
        "test_env": "dev",
    }