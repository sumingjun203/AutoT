# Calculator - pytest 单元测试项目

> 阶段一产出（Week 2 结束）
> 目标：第一个完整可运行的 pytest 项目

---

## 📋 项目说明

实现一个简单的计算器（加减乘除），用 pytest 编写完整的单元测试，练习：
- pytest 基本断言
- @pytest.mark.parametrize 参数化
- @pytest.fixture 资源管理
- conftest.py 共享 fixture
- pytest.ini 配置

---

## 🗂 目录结构

```
calculator/
├── src/
│   ├── __init__.py
│   └── calculator.py         # 计算器实现
├── tests/
│   ├── __init__.py
│   ├── conftest.py           # 共享 fixture
│   ├── test_add.py           # 加法测试
│   ├── test_subtract.py      # 减法测试
│   ├── test_multiply.py      # 乘法测试
│   ├── test_divide.py        # 除法测试
│   └── test_edge_cases.py    # 边界场景（除零、负数等）
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🎯 学习目标

- [ ] 实现 4 个基本运算函数（add、subtract、multiply、divide）
- [ ] 至少 15 个测试用例覆盖正常 + 异常
- [ ] 至少 3 处使用 parametrize
- [ ] 至少 2 个 fixture（function 级 + module 级）
- [ ] 1 个 conftest.py 共享 fixture
- [ ] pytest.ini 配置 testpaths、markers
- [ ] README 完整（项目说明、运行指南、覆盖截图）

---

## 🚀 快速开始

```bash
# 进入项目目录
cd projects/calculator

# 安装依赖（项目根目录已有 venv，这里只需要 pytest）
pip install pytest

# 运行测试
pytest -v

# 生成覆盖率报告（可选）
pip install pytest-cov
pytest --cov=src tests/
```

---

## ✅ 验收标准

- [ ] `pytest -v` 至少 15 个测试用例全部通过
- [ ] 至少 3 处 `@pytest.mark.parametrize`
- [ ] 至少 2 个 `@pytest.fixture`
- [ ] 边界场景：除零、负数、浮点精度
- [ ] 测试覆盖率 ≥ 90%
- [ ] README 完整

---

## 📝 实现示例（calculator.py）

```python
# src/calculator.py

class Calculator:
    """简单计算器实现"""

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("除数不能为零")
        return a / b
```

---

## 📚 参考

- pytest 官方文档：https://docs.pytest.org/en/stable/
- 项目计划：[`../../.omo/plans/python-auto-test-learning-plan.md`](../../.omo/plans/python-auto-test-learning-plan.md)

---

**开始时间**：待 Week 1 完成后
**目标完成**：Week 2 结束