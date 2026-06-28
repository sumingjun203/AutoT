# Saucedemo Demo - Selenium + POM 自动化测试

> 阶段二产出（Week 6 结束）
> 目标：完整可运行的 Selenium + Page Object Model 测试框架

---

## 📋 项目说明

针对经典练习网站 [https://www.saucedemo.com/](https://www.saucedemo.com/) 的完整 UI 自动化测试框架，演示：

- ✅ Selenium 4 + WebDriver Manager
- ✅ Page Object Model（POM）设计模式
- ✅ pytest fixture + 参数化
- ✅ YAML 数据驱动
- ✅ 失败自动截图
- ✅ loguru 日志
- ✅ Allure 报告

---

## 🗂 目录结构

```
saucedemo-demo/
├── pages/                          # 页面对象层
│   ├── __init__.py
│   ├── base_page.py                # BasePage 公共方法
│   ├── login_page.py               # 登录页
│   ├── inventory_page.py           # 商品列表页
│   ├── cart_page.py                # 购物车页
│   └── checkout_page.py            # 结算页
├── tests/
│   ├── __init__.py
│   ├── conftest.py                 # driver fixture + 截图 fixture
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── data/
│   └── login_data.yaml             # 登录测试数据
├── utils/
│   ├── __init__.py
│   ├── config.py                   # 配置读取
│   └── logger.py                   # loguru 封装
├── logs/                           # 日志输出
├── screenshots/                    # 失败截图
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🎯 学习目标

完成后您能：
- [ ] 独立设计并实现 POM 三层架构
- [ ] 处理 iframe、alert、下拉框等复杂场景
- [ ] 用 YAML 实现数据驱动
- [ ] 集成 loguru 日志 + 失败截图
- [ ] 集成 Allure 报告
- [ ] 至少 20 个测试用例

---

## 🚀 快速开始

```bash
# 进入项目目录
cd projects/saucedemo-demo

# 安装依赖
pip install -r requirements.txt

# 运行测试
pytest -v

# 运行并生成 Allure 报告
pytest --alluredir=./allure-results
allure serve ./allure-results

# 运行 smoke 标记
pytest -m smoke -v
```

---

## ✅ 验收标准

- [ ] 所有页面都通过 POM 封装
- [ ] 至少 20 个测试用例
- [ ] 数据驱动至少 2 处
- [ ] 失败自动截图
- [ ] 集成 loguru 日志
- [ ] 集成 Allure 报告
- [ ] README 完整（带 Allure 报告截图）

---

## 📚 设计要点

### BasePage 公共方法

```python
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        """封装元素定位 + 显式等待"""
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        self.find_element(locator).click()

    def input_text(self, locator, text):
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text
```

### Page 继承 BasePage

```python
class LoginPage(BasePage):
    # 定位器
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def login(self, username, password):
        self.input_text(self.USERNAME, username)
        self.input_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
        return InventoryPage(self.driver)
```

---

## 📚 参考

- 项目计划：[`../../.omo/plans/python-auto-test-learning-plan.md`](../../.omo/plans/python-auto-test-learning-plan.md)
- Selenium 官方：https://selenium-python.readthedocs.io/

---

**开始时间**：Week 3
**目标完成**：Week 6 结束