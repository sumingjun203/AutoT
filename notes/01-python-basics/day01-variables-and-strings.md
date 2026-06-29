# Day 1 - 变量、数据类型与字符串

> ⏱ 预计学习时长：1.5h
> 🎯 目标：能熟练定义变量、识别数据类型、灵活处理字符串（自动化场景必备基础）
> 📌 配套练习：见本文末尾"七、作业"

---

## 一、学习目标

完成本节后，你应该能：

- [x] 正确命名变量，识别合法 / 非法标识符
- [x] 区分 6 种常用数据类型（int / float / bool / str / None / 容器）
- [x] 用 `type()` 查看变量类型，理解隐式与显式转换
- [ ] 掌握字符串的 6 类操作：定义、索引、切片、拼接、方法、格式化
- [ ] 在自动化测试中熟练处理测试数据（用户名、URL、断言文本）

---

## 二、变量与赋值

### 2.1 变量的本质

> Python 是**动态类型**语言：变量本身没有类型，**值**才有类型。变量只是值的"标签"。

```python
# 同一个变量可以先后指向不同类型的值
x = 100        # x 指向 int
x = "hello"    # x 现在指向 str
x = [1, 2, 3]  # x 现在指向 list
```

### 2.2 命名规则（必须遵守）

| 规则 | 正确 ✅ | 错误 ❌ |
|------|--------|---------|
| 只能含字母、数字、下划线 | `user_name`, `age2` | `user-name`, `2age` |
| 不能以数字开头 | `_2024`, `name_2` | `2024_data` |
| 不能用关键字 | `class_`, `list_` | `class`, `list` |
| 区分大小写 | `Name ≠ name` | — |

### 2.3 命名约定（强烈推荐）

```python
# 普通变量：小写 + 下划线（snake_case）
user_name = "alice"
max_retry_count = 3

# 常量：全大写 + 下划线
DEFAULT_TIMEOUT = 10
BASE_URL = "https://example.com"

# 避免使用的名字
# l (小写 L)、I (大写 i)、O (大写 o) —— 容易和 1、0 混淆
```

### 2.4 多重赋值与解包

```python
# 同时赋值多个变量
a, b, c = 1, 2, 3

# 交换两个变量（Python 专属语法糖）
x, y = 10, 20
x, y = y, x      # 现在 x=20, y=10

# 链式赋值（所有变量指向同一个对象）
p = q = r = 0

# 解包（unpacking）
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5
```

### 2.5 `is` vs `==` 的区别（自动化面试常考）

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True —— 值相等
print(a is b)   # False —— 不是同一个对象（内存地址不同）
```

> **口诀**：`==` 比内容，`is` 比身份。判断 `None` 时永远用 `is` / `is not`。

---

## 三、数据类型

### 3.1 6 种核心类型速览

| 类型  | 关键字                         | 示例              | 可变性 | 用途          |
| --- | --------------------------- | --------------- | --- | ----------- |
| 整数  | `int`                       | `42`, `-7`, `0` | 不可变 | 计数、索引       |
| 浮点数 | `float`                     | `3.14`, `1e-3`  | 不可变 | 价格、比率       |
| 布尔  | `bool`                      | `True`, `False` | 不可变 | 条件、断言       |
| 字符串 | `str`                       | `"hello"`       | 不可变 | 文本处理        |
| 空值  | `NoneType`                  | `None`          | —   | 占位、缺省       |
| 容器  | `list`/`dict`/`set`/`tuple` | `[1,2]`         | 可变  | 数据集合（Day 4） |

### 3.2 查看类型与转换

```python
# type() 查看类型
print(type(42))        # <class 'int'>
print(type("hi"))      # <class 'str'>
print(type(None))      # <class 'NoneType'>

# isinstance() 推荐用于类型检查（考虑继承关系）
isinstance(3.14, (int, float))   # True

# 显式转换（casting）
int("100")       # 100
str(100)         # "100"
float("3.14")    # 3.14
bool(0)          # False
bool("")         # False
bool("hi")       # True
```

### 3.3 隐式转换的坑（自动化中要小心）

```python
# 整数 / 浮点运算 → 自动转 float
print(10 / 2)    # 5.0  （不是 5！）
print(10 // 2)   # 5    （整除）

# 布尔参与算术 → True=1, False=0
print(True + True)   # 2
print(False * 5)     # 0
```

### 3.4 `None` 不是 0、不是空字符串、不是 False

```python
result = None

# 正确：用 is 判断
if result is None:
    print("未执行")

# 错误：用 == 判断（PEP 8 明确反对）
if result == None:   # 能跑，但 pylint/flake8 会报警
    pass
```

---

## 四、字符串（自动化场景最高频）

### 4.1 三种定义方式

```python
s1 = 'hello'                  # 单引号
s2 = "hello"                  # 双引号
s3 = """hello
world"""                      # 三引号：可换行，常用于多行文本/docstring

# 含引号的字符串（用不同的引号包裹，或用转义）
text1 = "他说：'你好'"        # 外双内单
text2 = '他说："你好"'        # 外单内双
text3 = "他说：\"你好\""      # 转义
```

### 4.2 转义字符

```python
print("line1\nline2")   # \n 换行
print("a\tb")           # \t 制表符
print("C:\\path\\file") # \\ 反斜杠
print("他说：\"hi\"")   # \" 双引号
print(r"C:\new\test")   # r 前缀：原始字符串，不转义（路径、JSON 必备）
```

### 4.3 索引与切片（字符串不可变！）

```python
s = "Hello, World!"

# 索引：正向从 0，反向从 -1
print(s[0])        # 'H'
print(s[-1])       # '!'

# 切片：[start:stop:step]  含 start 不含 stop
print(s[0:5])      # 'Hello'
print(s[7:])       # 'World!'
print(s[:5])       # 'Hello'
print(s[::2])      # 'Hlo ol!'  —— 步长为 2
print(s[::-1])     # '!dlroW ,olleH'  —— 反转字符串（面试常考）

# ⚠️ 字符串不可变 —— 不能直接修改
# s[0] = 'h'   # TypeError: 'str' object does not support item assignment
new_s = "h" + s[1:]   # 正确：新建字符串
```

### 4.4 拼接与重复

```python
# + 拼接（少量字符串）
greeting = "Hello, " + "Alice" + "!"

# * 重复
echo = "=" * 30   # '=============================='

# ❌ 不推荐：循环里用 + 拼接（每次创建新对象，性能差）
result = ""
for item in ["a", "b", "c", "d"]:
    result += item     # 能用，但慢

# ✅ 推荐：用 join
result = "".join(["a", "b", "c", "d"])
```

### 4.5 常用方法（自动化测试必备 10 个）

| 方法 | 作用 | 示例 | 结果 |
|------|------|------|------|
| `s.strip()` | 去掉首尾空白 | `"  hi  ".strip()` | `"hi"` |
| `s.lower()` | 全小写 | `"Hello".lower()` | `"hello"` |
| `s.upper()` | 全大写 | `"Hi".upper()` | `"HI"` |
| `s.startswith(p)` | 是否以 p 开头 | `"https://a.com".startswith("https")` | `True` |
| `s.endswith(p)` | 是否以 p 结尾 | `"report.pdf".endswith(".pdf")` | `True` |
| `s.split(sep)` | 按分隔符切分 | `"a,b,c".split(",")` | `['a','b','c']` |
| `sep.join(list)` | 用分隔符拼接 | `",".join(['a','b'])` | `"a,b"` |
| `s.replace(old,new)` | 替换 | `"hi".replace("i","ello")` | `"hello"` |
| `s.find(sub)` | 找子串下标，找不到返 -1 | `"hello".find("ll")` | `2` |
| `s in big` | 包含判断 | `"ell" in "hello"` | `True` |

```python
# 实战：剥离 URL 参数
url = "https://api.example.com/login?token=abc123"
base, _, query = url.partition("?")   # ('https://...login', '?', 'token=abc123')
```

### 4.6 f-string 格式化（**Python 3.6+ 首选**）

```python
name = "Alice"
age = 30

# 基础用法 —— 变量插值
print(f"姓名：{name}，年龄：{age}")

# 表达式
print(f"明年 {age + 1} 岁")

# 格式化数字
price = 3.14159
print(f"价格：{price:.2f}")        # 保留 2 位小数："价格：3.14"
print(f"比例：{0.876:.1%}")        # 百分比："比例：87.6%"

# 对齐与填充（生成报告 / 日志超好用）
for i, item in enumerate(["登录", "查询", "登出"]):
    print(f"步骤 {i+1:0>2} | {item:<6} | OK")
# 步骤 01 | 登录     | OK   ← 中间 5 空格（:<6 在"登录"后补 4 格 + 字面 1 格）
# 步骤 02 | 查询     | OK
# 步骤 03 | 登出     | OK

# ⚠️ CJK 字符陷阱：Python 的 :<N 按字符数计算，不感知显示宽度
# "登录"占 2 字符 / 4 显示列，:<6 只补 4 个 ASCII 空格
# 在等宽字体终端里中文占 2 列宽，肉眼可能看着"差一格"
# 解决：手动加宽  `f"{item:<8}"`  或用 wcwidth / wcformat 库

# 调试技巧：等号 = 会同时打印变量名和值（Python 3.8+）
print(f"{name=}, {age=}")    # name='Alice', age=30
```

> 💡 **自动化测试中的价值**：f-string 让 `assert` 失败信息更清晰、报告更专业。

---

## 五、自动化测试中的应用场景

### 场景 1：构造测试数据

```python
username = f"test_user_{1001}"      # test_user_1001
email = f"{username}@example.com"
assert "@" in email
```

### 场景 2：URL 拼接

```python
BASE_URL = "https://api.example.com"
user_id = 42
url = f"{BASE_URL}/users/{user_id}/orders"
print(url)    # https://api.example.com/users/42/orders
```

### 场景 3：断言失败时给出可读信息

```python
actual = "Login successful"
expected = "Login Successful"

# ❌ 不好的断言
assert actual == expected

# ✅ 好的断言 + 调试信息
assert actual.lower() == expected.lower(), \
    f"断言失败: 实际='{actual}', 期望='{expected}'"
```

### 场景 4：从响应文本提取关键字段

```python
response_text = '{"name":"Alice","age":30}'
import json
data = json.loads(response_text)
assert data["name"].startswith("Ali"), f"name 不是以 Ali 开头: {data['name']}"
```

### 场景 5：处理配置文件路径（Windows / Linux 兼容）

```python
import os

# ❌ 硬编码路径
config_path = "C:\\Users\\test\\config.yaml"

# ✅ 用 os.path.join 跨平台
config_path = os.path.join("", "config.yaml")

# ✅ 用 pathlib（更现代，推荐）
from pathlib import Path
config_path = Path("data") / "config.yaml"
```

---

## 六、易错点速查（自动化测试常见 Bug）

| 错误 | 正确 | 原因 |
|------|------|------|
| `if x == None:` | `if x is None:` | PEP 8 规范 |
| `if name == "":` | `if not name:` | 更 Pythonic |
| `s[0] = "h"` | `new_s = "h" + s[1:]` | str 不可变 |
| `"a" + 1` | `"a" + str(1)` | str 和 int 不能直接 `+` |
| `10 / 2 == 5` | 用 `//` 或允许 `5.0` | `/` 永远返回 float |
| `assert isinstance(x, int)` | `assert type(x) is int`（视场景） | `bool` 是 `int` 子类 |
| `"hello".find("z") == 0` | `if "z" in "hello"` | find 找不到返回 -1 |

---

## 七、作业（必做 + 选做）

> ⏰ 预计用时：60-90 分钟
> 📍 提交位置：`projects/calculator/practice/day01/`（如不存在请创建）
> 💻 所有代码必须**在 Python 3.10+ 下运行通过**

### 基础题（必做）

#### 1. 变量交换
不使用第三个变量，交换 `a = 10`、`b = 20` 的值，并打印交换前后结果。

#### 2. 类型识别器
编写函数 `describe(value)`，根据输入返回字符串：
- `int` → `"整数: <值>"`
- `float` → `"浮点: <值>，保留 2 位 = <值:.2f>"`
- `str` → `"字符串: '<值>'，长度=<len>"`
- `bool` → `"布尔: <值>"`
- `None` → `"空值"`
- 其他 → `"未知类型: <类型名>"`

调用示例：
```python
print(describe(42))         # 整数: 42
print(describe(3.14159))    # 浮点: 3.14159，保留 2 位 = 3.14
print(describe("hi"))       # 字符串: 'hi'，长度=2
print(describe(True))       # 布尔: True
print(describe(None))       # 空值
```

#### 3. 温度转换器
编写函数 `celsius_to_fahrenheit(c)`，公式：`F = C × 9/5 + 32`。要求：
- 如果传入非数字（`int`/`float`），抛 `TypeError`
- 用 f-string 输出 `"{c}°C = {f}°F"`，保留 1 位小数

#### 4. 字符串工具箱
封装 5 个常用字符串工具函数（自动化测试必备）：

```python
def normalize(text: str) -> str:
    """去首尾空格 + 转小写"""

def is_chinese_phone(phone: str) -> bool:
    """判断是否为中国大陆手机号（11 位，1 开头）"""

def mask_email(email: str) -> str:
    """把邮箱用户名部分第 2 位之后替换为 *，例如 alice@x.com → a***e@x.com"""

def truncate(text: str, max_len: int = 20, suffix: str = "...") -> str:
    """超过 max_len 则截断并加 suffix"""

def extract_digits(text: str) -> str:
    """从字符串中提取所有数字，例如 '订单 ABC123 已发货' → '123'"""
```

#### 5. 身份证信息提取（自动化测试中的典型场景）
编写函数 `parse_id_card(id_card: str) -> dict`，从 18 位身份证号中提取：
- `birthday`：格式 `"YYYY-MM-DD"`（第 7-14 位）
- `gender`：`"男"` 或 `"女"`（第 17 位：奇男偶女）
- `region_code`：前 6 位

调用示例：
```python
print(parse_id_card("110101199003078811"))
# {'birthday': '1990-03-07', 'gender': '男', 'region_code': '110101'}
# 说明：身份证第 17 位（索引 16）是 '1'（奇数），按"奇男偶女"规则 → 男
# 速算小窍门：直接看第 17 位，1/3/5/7/9 → 男，0/2/4/6/8 → 女
```

### 进阶题（选做 1 道）

#### 6. 测试报告生成器
编写函数 `format_report(results: list[dict]) -> str`，输入形如：
```python
results = [
    {"name": "登录成功", "status": "PASS", "duration": 0.123},
    {"name": "查询订单", "status": "PASS", "duration": 0.456},
    {"name": "删除订单", "status": "FAIL", "duration": 0.089},
    {"name": "退出登录", "status": "PASS", "duration": 0.012},
]
```
输出对齐的报告（用 f-string 格式化，宽度自定义）：
```
用例名称        状态     耗时(s)
----------  --------  --------
登录成功       PASS     0.123
查询订单       PASS     0.456
删除订单       FAIL     0.089
退出登录       PASS     0.012
----------  --------  --------
通过: 3  失败: 1  总计: 4
```

### 挑战题（学有余力）

#### 7. 智能断言函数
封装一个通用的断言函数 `soft_assert(actual, expected, msg="")`，支持以下比较模式：
- 如果 `expected` 是 `bool`，直接断言 `bool(actual) == expected`
- 如果 `expected` 是数字，容差 `1e-6` 比较
- 如果 `expected` 是字符串，先 `strip().lower()` 再比较
- 断言失败时打印 f-string 格式化错误信息（包含 actual / expected / msg）
- 所有断言通过返回 `True`，失败抛 `AssertionError`

调用示例：
```python
soft_assert("  HELLO  ", "hello")                              # 通过
soft_assert(0.1 + 0.2, 0.3)                                    # 通过（浮点容差）
soft_assert([1, 2, 3], True)                                   # 通过（非空列表为真）
soft_assert("Login Success", "login success", "登录接口")        # 通过
soft_assert("actual", "expected", "关键文本")                   # 失败，抛异常
```

---

## 八、自检清单（完成作业后勾选）

- [ ] 我能区分 `is` 和 `==`
- [ ] 我能用 `type()` 和 `isinstance()` 判断类型
- [ ] 我能解释 `10 / 2` 为什么是 `5.0` 而不是 `5`
- [ ] 我能用 f-string 格式化数字、对齐文本
- [ ] 我能用 `strip`/`split`/`join`/`replace`/`startswith` 处理字符串
- [ ] 我能解释为什么字符串不可变
- [ ] 我能为今天写的所有函数加上类型注解

---

## 九、明日预告

**Day 2 - 控制流（if / for / while / 列表推导式）**
- 实战：用 `for` + `if` 写一个断言工具集
- 实战：九九乘法表（列表推导式）
- 实战：用 `while` 实现重试机制（自动化测试常用）

---

## 📚 参考资料

- [Python 官方教程 - 字符串](https://docs.python.org/zh-cn/3/tutorial/introduction.html#strings)
- [PEP 8 - 编码风格](https://peps.python.org/pep-0008/)
- [f-string 官方说明](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html#formatted-string-literals)

---

**完成时间**：____ / ____ / ____
**自评**：⭐⭐⭐⭐⭐（1-5 星）
**卡点**：_________________________________________________