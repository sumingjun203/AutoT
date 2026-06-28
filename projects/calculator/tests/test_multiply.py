"""
test_multiply.py - 乘法测试用例
"""
import pytest

from src.calculator import multiply


class TestMultiply:
    """乘法测试类"""

    def test_multiply_positive(self, calc):
        """正数相乘"""
        assert calc.multiply(3, 4) == 12

    def test_multiply_by_zero(self, calc):
        """任何数乘以零都为零"""
        assert calc.multiply(5, 0) == 0
        assert calc.multiply(0, 5) == 0

    def test_multiply_negative(self, calc):
        """负数相乘"""
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(-2, -3) == 6

    @pytest.mark.parametrize("a,b,expected", [
        (3, 4, 12),
        (0, 100, 0),
        (-2, 3, -6),
        (-2, -3, 6),
        (2.5, 4, 10.0),
    ])
    def test_multiply_parametrize(self, a, b, expected):
        """参数化测试"""
        assert multiply(a, b) == expected