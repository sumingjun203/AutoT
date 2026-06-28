"""
test_subtract.py - 减法测试用例
"""
import pytest

from src.calculator import subtract


class TestSubtract:
    """减法测试类"""

    def test_subtract_positive(self, calc):
        """正数相减"""
        assert calc.subtract(10, 3) == 7

    def test_subtract_to_negative(self, calc):
        """结果为负"""
        assert calc.subtract(3, 10) == -7

    def test_subtract_zero(self, calc):
        """减零"""
        assert calc.subtract(5, 0) == 5
        assert calc.subtract(0, 5) == -5

    @pytest.mark.parametrize("a,b,expected", [
        (10, 3, 7),
        (3, 10, -7),
        (0, 0, 0),
        (-5, -5, 0),
        (100, 50, 50),
    ])
    def test_subtract_parametrize(self, a, b, expected):
        """参数化测试"""
        assert subtract(a, b) == expected