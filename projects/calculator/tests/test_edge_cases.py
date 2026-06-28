"""
test_edge_cases.py - 边界场景测试

覆盖一些容易遗漏的边界情况。
"""
import pytest

from src.calculator import Calculator


class TestEdgeCases:
    """边界场景"""

    def test_very_large_numbers(self, calc):
        """极大数相加"""
        result = calc.add(10**100, 10**100)
        assert result == 2 * 10**100

    def test_very_small_numbers(self, calc, config):
        """极小数相减"""
        result = calc.subtract(0.00001, 0.00002)
        assert abs(result - (-0.00001)) < config["tolerance"]

    def test_mixed_types_via_int(self, calc):
        """int + float 应该返回 float"""
        result = calc.add(1, 2.5)
        assert result == 3.5
        assert isinstance(result, float)

    def test_chained_operations(self, calc):
        """链式运算"""
        # (1 + 2) * 3 - 4 = 5
        result = calc.subtract(calc.multiply(calc.add(1, 2), 3), 4)
        assert result == 5

    @pytest.mark.smoke
    def test_smoke_all_operations(self, calc):
        """冒烟测试：所有基本运算跑一遍"""
        assert calc.add(1, 1) == 2
        assert calc.subtract(5, 3) == 2
        assert calc.multiply(2, 3) == 6
        assert calc.divide(10, 2) == 5