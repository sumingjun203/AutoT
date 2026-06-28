"""
test_add.py - 加法测试用例
"""
import pytest

from src.calculator import add


class TestAdd:
    """加法测试类"""

    def test_add_positive_numbers(self, calc):
        """正数相加"""
        assert calc.add(2, 3) == 5

    def test_add_negative_numbers(self, calc):
        """负数相加"""
        assert calc.add(-1, -2) == -3

    def test_add_zero(self, calc):
        """与零相加"""
        assert calc.add(0, 5) == 5
        assert calc.add(5, 0) == 5
        assert calc.add(0, 0) == 0

    def test_add_float(self, calc, config):
        """浮点数相加（使用 tolerance）"""
        result = calc.add(0.1, 0.2)
        assert abs(result - 0.3) < config["tolerance"]

    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 3),
        (10, 20, 30),
        (-5, 5, 0),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
    ])
    def test_add_parametrize(self, a, b, expected):
        """参数化测试：多个加法组合"""
        assert add(a, b) == pytest.approx(expected)