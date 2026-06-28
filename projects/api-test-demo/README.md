# API Test Demo - requests + pytest 自动化测试

> 阶段三产出（Week 10 结束）
> 目标：完整可运行的 API 自动化测试框架

---

## 📋 项目说明

针对 https://reqres.in/ 的完整 API 自动化测试框架，演示：

- ✅ requests 库 + Session
- ✅ pytest fixture + 参数化
- ✅ YAML 数据驱动
- ✅ 鉴权处理（Bearer Token）
- ✅ 接口关联（响应提取 + 注入）
- ✅ Mock 测试（unittest.mock）
- ✅ Allure 报告
- ✅ loguru 日志

---

## 🗂 目录结构

```
api-test-demo/
├── api/                          # 接口封装层
│   ├── __init__.py
│   ├── base_api.py              # BaseAPI 公共方法
│   ├── user_api.py              # 用户相关接口
│   ├── auth_api.py              # 鉴权相关接口
│   └── order_api.py             # 订单相关接口
├── testcases/
│   ├── __init__.py
│   ├── conftest.py              # 共享 fixture
│   ├── test_user.py
│   ├── test_auth.py
│   └── test_order.py
├── data/
│   ├── user_data.yaml
│   ├── auth_data.yaml
│   └── order_data.yaml
├── utils/
│   ├── __init__.py
│   ├── config.py                # 配置管理
│   ├── logger.py                # 日志
│   ├── read_yaml.py             # YAML 读取工具
│   └── assertions.py            # 自定义断言
├── config/
│   └── config.yaml              # 全局配置
├── logs/                        # 日志
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🎯 学习目标

完成后您能：
- [ ] 设计 API 分层架构（封装层 + 测试层）
- [ ] 处理 Bearer Token / Session / Cookie 鉴权
- [ ] 用 jsonpath 提取响应字段
- [ ] 用 Mock 解耦外部依赖
- [ ] 用 YAML 实现数据驱动
- [ ] 至少 30 个测试用例

---

## 🚀 快速开始

```bash
# 进入项目目录
cd projects/api-test-demo

# 安装依赖
pip install -r requirements.txt

# 运行测试
pytest -v

# 运行并生成 Allure 报告
pytest --alluredir=./allure-results
allure serve ./allure-results

# 运行指定模块
pytest testcases/test_user.py -v
```

---

## ✅ 验收标准

- [ ] BaseAPI 封装：统一处理请求、鉴权、响应断言
- [ ] 至少 3 个 API 模块（auth、user、order）
- [ ] 至少 30 个测试用例
- [ ] 包含鉴权处理（Token 提取 + 注入）
- [ ] 至少 2 处接口关联
- [ ] 至少 1 处 Mock
- [ ] 集成 Allure 报告
- [ ] README 完整

---

## 📚 设计要点

### BaseAPI 公共方法

```python
class BaseAPI:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://reqres.in/api"

    def _request(self, method, url, **kwargs):
        resp = self.session.request(method, url, **kwargs)
        return resp

    def get(self, endpoint, **kwargs):
        return self._request("GET", f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", f"{self.base_url}{endpoint}", **kwargs)
```

### 鉴权装饰器

```python
def auth_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # 自动添加 Token
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {self.token}"
        kwargs["headers"] = headers
        return func(self, *args, **kwargs)
    return wrapper
```

---

## 📚 参考

- 项目计划：[`../../.omo/plans/python-auto-test-learning-plan.md`](../../.omo/plans/python-auto-test-learning-plan.md)
- requests 官方：https://requests.readthedocs.io/

---

**开始时间**：Week 7
**目标完成**：Week 10 结束