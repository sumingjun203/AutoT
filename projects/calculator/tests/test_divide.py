"""
test_divide.py - 除法测试用例
"""
import pytest

from src.calculator import divide


class TestDivide:
    """除法测试类"""

    def test_divide_positive(self, calc):
        """正数相除"""
        assert calc.divide(10, 2) == 5

    def test_divide_to_float(self, calc, config):
        """结果为浮点数"""
        result = calc.divide(10, 3)
        assert abs(result - 3.3333) < config["tolerance"]

    def test_divide_zero_raises(self, calc):
        """除以零应该抛出异常"""
        with pytest.raises(ZeroDivisionError) as exc_info:
            calc.divide(10, 0)
        assert "除数不能为零" in str(exc_info.value)

    @pytest.mark.parametrize("a,b,expected", [
        (10, 2, 5),
        (100, 10, 10),
        (-10, 2, -5),
        (-10, -2, 5),
    ])
    def test_divide_parametrize(self, a, b, expected):
        """参数化测试"""
        assert divide(a, b) == expected

    @pytest.mark.parametrize("a,b", [
        (10, 0),
        (0, 0),
        (-5, 0),
    ])
    def test_divide_by_zero_parametrize(self, a, b):
        """参数化：多种除零场景"""
        with pytest.raises(ZeroDivisionError):
            divide(a, b)