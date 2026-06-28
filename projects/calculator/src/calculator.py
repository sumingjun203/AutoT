"""
calculator.py - 简单计算器实现

这是阶段一 Week 2 的实战项目源码。
"""


class Calculator:
    """简单计算器：实现加减乘除四个基本运算"""

    @staticmethod
    def add(a: float, b: float) -> float:
        """加法"""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """减法"""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """乘法"""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """除法"""
        if b == 0:
            raise ZeroDivisionError("除数不能为零")
        return a / b


# 模块级函数（方便直接调用）
def add(a, b):
    return Calculator.add(a, b)


def subtract(a, b):
    return Calculator.subtract(a, b)


def multiply(a, b):
    return Calculator.multiply(a, b)


def divide(a, b):
    return Calculator.divide(a, b)