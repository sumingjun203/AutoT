# Python 自动化测试学习计划

> 为测试工程师定制的 2-3 个月系统学习路径
> 目标：掌握 Selenium Web UI 自动化 + requests API 自动化，能在公司项目中独立交付

---

## TL;DR

> **学习者画像**：入门级 Python + Postman 经验，目标 Web UI + API 双方向，2-3 个月系统学习
>
> **核心交付物**：
> - ✅ GitHub 个人作品集（2 个完整开源项目）
> - ✅ 完整学习笔记（Markdown 知识库）
> - ✅ 公司项目可直接复用的测试框架
>
> **技术栈**：pytest + Selenium + requests + Allure + POM + GitHub Actions
>
> **学习周期**：13 周（5 个阶段），每周 8-12 小时（工作日 1-2h + 周末 4-6h）
>
> **关键里程碑**：
> - Week 2 结束：能写 pytest 单元测试
> - Week 6 结束：能搭建 Selenium + POM 框架
> - Week 10 结束：能搭建完整 API 测试框架
> - Week 13 结束：作品集 + 笔记全部完成

---

## Context

### 您的起点

| 维度 | 现状 | 说明 |
|------|------|------|
| Python | 入门级 | 有基础但生疏，需快速过一遍语法 |
| 测试经验 | Postman 手动测试 | 没系统做过自动化 |
| 公司栈 | 传统 Web（jQuery/Vue2） | 元素定位可能有 iframe、复杂 DOM |
| API 类型 | REST + 鉴权 + 文件 | 全场景覆盖 |
| 学习方式 | 官方文档 + 实战 | 拒绝只看不练 |
| 时间 | 工作日 1-2h + 周末集中 | 约 8-12h/周 |

### 关键决策与理由

| 决策 | 选择 | 理由 |
|------|------|------|
| 测试框架 | **pytest** | 行业事实标准，简洁强大，插件丰富 |
| Web 工具 | **Selenium**（不用 Playwright） | 您指定，与公司框架保持一致 |
| API 库 | **requests** | Python API 测试事实标准，文档完善 |
| 报告 | **Allure** | 行业标准可视化报告，求职加分项 |
| 设计模式 | **Page Object Model (POM)** | 企业级必备技能 |
| 笔记工具 | Markdown + Git | 可沉淀、可分享、可版本管理 |

---

## Work Objectives

### 核心目标

> **2-3 个月内，从"会手动测试"成长为"能独立设计并交付自动化测试框架"的工程师。**

### 具体能力指标

完成后您将能：

1. ✅ 独立搭建 pytest 测试项目（含 conftest、fixture、参数化）
2. ✅ 用 Selenium + POM 设计 Web UI 自动化框架
3. ✅ 用 requests 设计 API 自动化框架（含鉴权、数据驱动、Mock）
4. ✅ 集成 Allure 生成专业测试报告
5. ✅ 用 GitHub Actions 实现 CI/CD 自动跑测试
6. ✅ 在 GitHub 上展示 2 个完整可运行的开源测试项目
7. ✅ 拥有结构化的 Markdown 知识库（可二次复习 + 面试参考）

### Definition of Done

- [ ] **作品集 A**：Selenium + POM 完整 Web 测试框架（GitHub 公开仓库）
- [ ] **作品集 B**：requests + pytest API 测试框架（GitHub 公开仓库）
- [ ] **知识库**：每个阶段的 Markdown 笔记，存放在 `notes/` 目录
- [ ] **博客/总结**：撰写 1-2 篇方法论总结（可选，但面试加分）
- [ ] **面试题清单**：50+ 常见 Python 自动化测试面试题 + 答案

---

## 学习路径总览

```
┌─────────────────────────────────────────────────────────┐
│  阶段一 (Week 1-2)  Python 速成 + pytest 入门          │
│  ─────────────────────────────────────────────────     │
│  目标：能写基础 pytest 单元测试                          │
└────────────────────────┬────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  阶段二 (Week 3-6)  Selenium Web UI 自动化              │
│  ─────────────────────────────────────────────────     │
│  目标：能用 POM 模式搭建 Web 自动化框架                  │
└────────────────────────┬────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  阶段三 (Week 7-10)  requests API 自动化                 │
│  ─────────────────────────────────────────────────     │
│  目标：能搭建含鉴权、数据驱动的 API 测试框架             │
└────────────────────────┬────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  阶段四 (Week 11-12) 整合 + 报告 + CI/CD                │
│  ─────────────────────────────────────────────────     │
│  目标：Allure 报告 + GitHub Actions 自动化              │
└────────────────────────┬────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  阶段五 (Week 12-13) 作品集 + 知识沉淀                  │
│  ─────────────────────────────────────────────────     │
│  目标：GitHub 仓库 + 完整笔记 + 面试准备                 │
└─────────────────────────────────────────────────────────┘
```

---

## 阶段一：Python 速成 + pytest 入门（Week 1-2）

### 学习目标

- 复习 Python 核心语法（聚焦测试场景）
- 掌握 pip、venv、requirements.txt
- 掌握 pytest 基本用法（断言、参数化、fixture 入门）
- 完成第一个可运行的测试项目

### 每日时间分配（工作日 1-2h）

| 时段 | 内容 | 时长 |
|------|------|------|
| 周一晚 | Python 语法复习（数据类型、控制流、函数） | 1.5h |
| 周二晚 | Python 复习（类、异常、模块） | 1.5h |
| 周三晚 | pip/venv 环境管理 + 第一个 pytest 用例 | 1.5h |
| 周四晚 | pytest 断言、参数化、fixture | 1.5h |
| 周五晚 | 周末任务预研 / 自由练习 | 1h |
| 周末 | 综合实战（4-6h） | 4-6h |

### Week 1：Python 核心语法速成

**核心内容**（每天一个小主题）：

| 天 | 主题 | 必学知识点 | 练习 |
|----|------|-----------|------|
| Day 1 | 基础语法 | 变量、数据类型、字符串格式化（f-string） | 写 10 个字符串处理函数 |
| Day 2 | 控制流 | if/else、for、while、列表推导式 | 写一个九九乘法表 |
| Day 3 | 函数 | def、参数（默认/可变/*args/**kwargs）、返回值、lambda | 写 5 个工具函数 |
| Day 4 | 数据结构 | list/tuple/dict/set 的 CRUD、嵌套 | 写一个通讯录管理程序 |
| Day 5 | 类与对象 | class、__init__、self、继承、魔术方法 | 写一个简单的 User 类 |
| Day 6-7（周末） | 综合复习 | 异常处理（try/except）、文件操作、模块导入 | 完成一个 Todo List 小项目 |

**学习资源**：
- 官方文档：https://docs.python.org/zh-cn/3/tutorial/
- 推荐：廖雪峰 Python 教程（基础部分快速过）
- 速查表：https://www.pythoncheatsheet.org/

### Week 2：pytest 入门

**核心内容**：

| 天 | 主题 | 必学知识点 |
|----|------|-----------|
| Day 8 | pytest 基础 | 安装、第一个测试用例、命名规则（test_*.py）、pytest 收集规则 |
| Day 9 | 断言与异常 | assert 用法、pytest.raises() 捕获异常、assert 失败信息解读 |
| Day 10 | 参数化 | @pytest.mark.parametrize、参数组合、ids 用法 |
| Day 11 | fixture 入门 | @pytest.fixture、scope（function/class/module/session）、yield 清理 |
| Day 12 | 配置与命令行 | pytest.ini、conftest.py、常用命令行参数（-v、-k、-x、--maxfail） |
| Day 13-14 | 综合实战 | 搭建第一个 pytest 项目结构 |

**项目 1：pytest 单元测试项目（calculator）**

```
calculator/
├── src/
│   └── calculator.py        # 实现加减乘除
├── tests/
│   ├── test_add.py
│   ├── test_subtract.py
│   ├── conftest.py
│   └── test_calc_parametrize.py
├── pytest.ini
├── requirements.txt
└── README.md
```

**验收标准**：
- [ ] `pytest -v` 至少 10 个测试用例全部通过
- [ ] 至少 3 个测试用例使用 parametrize
- [ ] 至少 2 个 fixture（一个 function 级，一个 module 级）
- [ ] 能在命令行看到清晰的 pass/fail 报告

### 阶段一产出

- ✅ 第一个 GitHub 仓库（calculator）
- ✅ Python 语法速记笔记
- ✅ pytest 基础笔记

---

## 阶段二：Selenium Web UI 自动化（Week 3-6）

### 学习目标

- 掌握 Selenium WebDriver 核心 API
- 掌握 8 种元素定位方式（重点：xpath、css_selector）
- 掌握三种等待机制（解决老 Web 应用异步加载问题）
- 掌握 iframe、alert、下拉框等特殊场景处理
- 掌握 Page Object Model（POM）设计模式
- 独立搭建完整的 Selenium 测试框架

### Week 3：Selenium 基础

**核心内容**：

| 天 | 主题 | 必学知识点 |
|----|------|-----------|
| Day 15 | 环境搭建 | 安装 selenium、配置 WebDriver（推荐 webdriver-manager）、浏览器选择 |
| Day 16 | 8 种定位 | id / name / class_name / tag_name / link_text / partial_link_text / xpath / css_selector |
| Day 17 | 常用操作 | 点击、输入、清空、获取文本/属性、浏览器操作（前进/后退/刷新/最大化） |
| Day 18 | 等待机制 | time.sleep() / implicitly_wait() / WebDriverWait + expected_conditions（重点） |
| Day 19 | 高级交互 | 鼠标（ActionChains）、键盘（Keys）、下拉框（Select）、iframe 切换 |
| Day 20-21 | 弹窗与文件 | alert/confirm/prompt、文件上传、截图（save_screenshot） |

**练习项目**：对 https://www.saucedemo.com/ 做 5 个测试用例
- 登录成功/失败
- 商品排序
- 加入购物车
- 下单流程（至少 2 步）
- 截图保存

**学习资源**：
- Selenium 官方文档：https://selenium-python.readthedocs.io/
- 推荐：https://www.selenium.dev/documentation/

### Week 4：pytest + Selenium 整合 + POM 入门

**核心内容**：

| 天 | 主题 | 必学知识点 |
|----|------|-----------|
| Day 22 | 项目结构 | 设计分层：pages/、tests/、utils/、conftest.py |
| Day 23 | fixture 进阶 | conftest.py 共享 driver、yield 清理、scope 控制 |
| Day 24 | POM 概念 | 为什么要用 POM、Page 类设计、元素 + 操作封装 |
| Day 25 | POM 实战 | BasePage 公共方法（click、send_keys、wait）、LoginPage 实战 |
| Day 26 | 数据驱动 | 从 YAML/JSON 读取测试数据、参数化 |
| Day 27-28 | 综合实战 | 搭建第一个完整 POM 项目 |

**项目 2：Selenium POM 测试框架（saucedemo-demo）**

```
saucedemo-demo/
├── pages/
│   ├── base_page.py         # 公共方法
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/
│   ├── conftest.py          # driver fixture
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_cart.py
├── data/
│   └── login_data.yaml
├── utils/
│   └── config.py
├── pytest.ini
├── requirements.txt
└── README.md
```

**验收标准**：
- [ ] 所有页面都通过 POM 封装
- [ ] 至少 15 个测试用例
- [ ] 数据驱动至少 2 处
- [ ] 失败用例自动截图

### Week 5-6：POM 进阶 + 公司项目实战

**Week 5 学习内容**：

| 主题 | 必学 |
|------|------|
| 复杂场景 | iframe 多层嵌套、Shadow DOM、JavaScript 弹窗处理 |
| 高级等待 | 自定义 expected_conditions、轮询机制 |
| 错误处理 | 异常重试机制、失败截图、page source 保存 |
| 日志 | logging 模块集成、loguru（推荐） |
| 浏览器配置 | 无头模式、禁用图片、用户代理、代理 IP |

**Week 6：综合实战（最关键的一周）**

在公司项目中找到**一个真实模块**（如：登录 + 个人中心），用 Selenium + POM 完整覆盖：

- 至少 20 个测试用例
- 包含正向（happy path）+ 反向（异常分支）
- 集成 Allure 报告
- 失败自动截图
- 集成 logging 日志

### 阶段二产出

- ✅ saucedemo-demo GitHub 仓库（公开）
- ✅ 公司项目实战 demo（可内部分享）
- ✅ Selenium 元素定位速记表
- ✅ POM 设计模式笔记

---

## 阶段三：requests API 自动化（Week 7-10）

### 学习目标

- 掌握 HTTP 协议核心概念（您有 Postman 经验，会很快）
- 掌握 requests 库全部常用 API
- 处理鉴权（Token / Cookie / Session / JWT）
- 处理文件上传下载
- 掌握接口自动化框架设计（分层 + 数据驱动 + Mock）
- 独立搭建完整 API 测试框架

### Week 7：requests 基础

**核心内容**：

| 天 | 主题 | 必学知识点 |
|----|------|-----------|
| Day 43 | HTTP 回顾 | 请求方法、状态码分类、Header、Cookie（您熟悉 Postman，会很快） |
| Day 44 | requests 基础 | requests.get/post/put/delete、params、data、json、headers、timeout |
| Day 45 | 响应处理 | response.status_code / text / content / json() / headers / cookies |
| Day 46 | Session 会话 | requests.Session() 跨请求保持 Cookie、自动管理鉴权 |
| Day 47 | 鉴权处理 | Token（Bearer）、Basic Auth、Cookie、Session、签名（HMAC 入门） |
| Day 48-49 | 文件操作 | 文件上传（files 参数）、多文件、断点续传、文件下载（stream + chunk） |

**练习项目**：对 https://httpbin.org/ 或公司测试环境做 10 个 API 测试用例

**学习资源**：
- requests 官方文档：https://requests.readthedocs.io/zh_CN/latest/
- 推荐：https://realpython.com/python-requests/

### Week 8：pytest + requests + 数据驱动

**核心内容**：

| 天 | 主题 | 必学知识点 |
|----|------|-----------|
| Day 50 | 项目结构 | 设计 API 框架：api/（封装层）、testcases/（测试层）、data/、utils/ |
| Day 51 | API 封装层 | 封装 requests、抽象 BaseAPI、统一处理鉴权、统一断言 |
| Day 52 | 数据驱动进阶 | YAML 嵌套参数、JSON Schema 校验、参数化数据源 |
| Day 53 | 接口关联 | 上一个接口响应提取（jsonpath / 正则）、全局变量管理 |
| Day 54 | fixture 进阶 | conftest 多层共享、factory fixture、参数化 fixture |
| Day 55-56 | 综合实战 | 搭建第一个完整 API 框架 |

**项目 3：API 测试框架（api-test-demo）**

```
api-test-demo/
├── api/                    # 接口封装层
│   ├── base_api.py
│   ├── user_api.py
│   ├── order_api.py
│   └── auth_api.py
├── testcases/
│   ├── conftest.py
│   ├── test_user.py
│   ├── test_order.py
│   └── test_auth.py
├── data/
│   ├── user_data.yaml
│   └── order_data.yaml
├── utils/
│   ├── handle_token.py
│   ├── read_yaml.py
│   └── assertions.py
├── config/
│   └── config.yaml
├── pytest.ini
├── requirements.txt
└── README.md
```

**验收标准**：
- [ ] 至少 20 个 API 测试用例
- [ ] 至少 3 个模块（登录、用户、订单）
- [ ] 包含鉴权处理（Token 提取 + 注入）
- [ ] 至少 2 处接口关联
- [ ] 集成 Allure 报告

### Week 9：Mock 测试 + 高级场景

**核心内容**：

| 主题 | 必学 |
|------|------|
| unittest.mock | Mock 对象、patch 装饰器、side_effect、return_value |
| responses 库 | Mock HTTP 响应、模拟第三方依赖 |
| 复杂场景 | 接口签名验证、HTTPS 证书、代理、超时重试 |
| 数据库验证 | pymysql / pymongo 验证接口写入数据 |
| 性能基础 | 接口响应时间断言（locust 入门，下阶段深入） |

### Week 10：公司项目 API 实战

在公司项目中找到**一个完整业务流**（如：登录 → 创建订单 → 查询订单 → 取消订单），用 API 框架完整覆盖：

- 至少 30 个测试用例
- 完整鉴权链
- 至少 5 处接口关联
- 集成 Allure
- 包含正向 + 异常场景

### 阶段三产出

- ✅ api-test-demo GitHub 仓库
- ✅ 公司项目 API 实战
- ✅ requests 速记表
- ✅ HTTP 协议 + 鉴权笔记

---

## 阶段四：整合 + 报告 + CI/CD（Week 11-12）

### 学习目标

- 集成 Allure 生成专业测试报告
- 掌握 Git + GitHub 协作流程
- 掌握 GitHub Actions 持续集成
- 掌握测试用例失败重试、并发执行
- 完整整合 UI + API 测试

### Week 11：Allure 报告 + 日志

**核心内容**：

| 主题 | 必学 |
|------|------|
| Allure 安装 | allure-pytest 安装、Allure Commandline 配置（Windows / Mac） |
| Allure 用法 | @allure.title / @allure.feature / @allure.story / @allure.step |
| 报告装饰 | @allure.description、严重级别、附件（截图、log） |
| 历史趋势 | allure-results 持久化、趋势图 |
| 日志整合 | loguru 集成、Allure 附加日志 |

**实战**：为阶段二、三的项目集成 Allure

### Week 12：CI/CD + 整合测试

**核心内容**：

| 主题 | 必学 |
|------|------|
| Git 进阶 | branch / merge / rebase / cherry-pick / 冲突解决 |
| GitHub 协作 | Pull Request、Code Review、Issue |
| GitHub Actions | workflow 语法、jobs / steps / runs-on |
| 自动化跑测 | push 触发测试、定时任务、矩阵测试 |
| 通知 | Slack / 邮件 / 飞书 / 钉钉通知 |
| 测试报告发布 | Allure Report 部署到 GitHub Pages |

**实战项目**：为 saucedemo-demo 配 GitHub Actions

```yaml
# .github/workflows/test.yml
name: Selenium Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install -r requirements.txt
      - run: pytest --alluredir=./allure-results
      - uses: simple-elf/allure-report-action@master
        if: always()
        with:
          allure_results: ./allure-results
          allure_history: allure-history
```

### 阶段四产出

- ✅ Allure 报告截图（GitHub 仓库 README 展示）
- ✅ GitHub Actions 配置文件
- ✅ CI/CD 笔记

---

## 阶段五：作品集 + 知识沉淀（Week 12-13，最后一周）

### 学习目标

- 整理 2 个完整作品集（README + 文档 + 代码）
- 完成结构化知识库
- 整理常见面试题
- 输出 1-2 篇方法论总结（可选）

### Week 13 任务清单

| 任务 | 时长 | 输出 |
|------|------|------|
| 完善 saucedemo-demo 仓库 | 2h | README 包含：项目介绍、架构图、运行指南、效果截图 |
| 完善 api-test-demo 仓库 | 2h | 同上 |
| 整理知识库目录 | 3h | notes/ 目录 + README 索引 |
| 50 道面试题 | 4h | notes/interview/ 目录 + 答案 |
| 撰写方法论博客（可选） | 2h | "如何从零搭建自动化测试框架" |
| 简历 + 自我介绍 | 1h | 整合到简历项目经验 |

### 推荐的知识库结构

```
notes/
├── README.md                 # 导航
├── 01-python-basics/         # Python 速记
├── 02-pytest/                # pytest 笔记
├── 03-selenium/              # Selenium 笔记
│   ├── locator-cheatsheet.md
│   ├── waits-cheatsheet.md
│   └── pom-design.md
├── 04-requests/              # API 笔记
│   ├── http-basics.md
│   ├── auth-handling.md
│   └── api-framework-design.md
├── 05-allure/                # 报告
├── 06-cicd/                  # CI/CD
├── 07-interview/             # 面试题
│   ├── python-basics.md
│   ├── pytest.md
│   ├── selenium.md
│   └── framework-design.md
└── 08-mindmap/               # 知识图谱
```

### 推荐的 2 个 GitHub 仓库

| 仓库 | 内容 | 亮点 |
|------|------|------|
| **saucedemo-demo** | Selenium + POM + pytest + Allure + GitHub Actions | 完整 CI 流程，可在线看 Allure 报告 |
| **api-test-demo** | requests + pytest + 数据驱动 + Allure + GitHub Actions | 含鉴权、MOCK、关联测试 |

两个仓库 README 应包含：
- 项目简介 + 架构图
- 技术栈徽章（shields.io）
- 快速开始指南
- 测试报告截图
- 后续可优化方向

---

## 学习资源清单

### 官方文档（首选）

| 资源 | 链接 | 用途 |
|------|------|------|
| Python 官方 | https://docs.python.org/zh-cn/3/ | 语法参考 |
| pytest 官方 | https://docs.pytest.org/en/stable/ | pytest 权威 |
| Selenium Python | https://selenium-python.readthedocs.io/ | Selenium 权威 |
| requests 官方 | https://requests.readthedocs.io/ | requests 权威 |
| Allure 官方 | https://allurereport.org/docs/ | Allure 报告 |
| GitHub Actions | https://docs.github.com/actions | CI/CD |

### 工具与库

| 工具 | 用途 | 安装命令 |
|------|------|---------|
| pytest | 测试框架 | `pip install pytest` |
| selenium | Web 自动化 | `pip install selenium` |
| webdriver-manager | 自动管理驱动 | `pip install webdriver-manager` |
| requests | HTTP 客户端 | `pip install requests` |
| PyYAML | YAML 解析 | `pip install pyyaml` |
| allure-pytest | Allure 集成 | `pip install allure-pytest` |
| loguru | 更好用的日志 | `pip install loguru` |
| pytest-rerunfailures | 失败重试 | `pip install pytest-rerunfailures` |
| pytest-xdist | 并发执行 | `pip install pytest-xdist` |
| responses | HTTP Mock | `pip install responses` |

### 实战练习网站

| 网站 | 用途 |
|------|------|
| https://www.saucedemo.com/ | Selenium 经典练习场 |
| https://httpbin.org/ | API 测试练习场 |
| https://reqres.in/ | 真实场景 API 模拟 |
| https://the-internet.herokuapp.com/ | 综合 Web 元素场景 |
| https://practice.expandtesting.com/ | 多种测试场景 |

---

## 风险与应对

| 风险 | 概率 | 应对策略 |
|------|------|---------|
| 学到一半放弃 | 中 | 每周设小目标 + 番茄钟 + 找学习搭子 |
| 学完不会用 | 中 | **强制要求每个阶段有实战项目**（边学边用） |
| 公司项目无法实战 | 高 | 用 https://the-internet.herokuapp.com/ 等替代 |
| 知识点太多记不住 | 高 | 持续更新 Markdown 笔记（边学边记） |
| 遇到问题卡住 | 中 | 优先：官方文档 → Stack Overflow → CSDN/掘金 → 问 AI |
| 浏览器驱动版本问题 | 中 | 用 webdriver-manager 自动管理 |

### 心态建议

> **不要追求完美，不要追求学完所有知识**。
> 自动化测试的核心是"**用工具解决重复劳动**"，不是炫技。
> 您的目标是：**能在 2-3 个月后用所学解决公司实际问题**。

---

## 验收标准（结业标准）

### 硬性指标

- [ ] 2 个公开 GitHub 仓库（UI + API），每个至少 30 个测试用例
- [ ] 每个仓库有完整 README + Allure 报告截图
- [ ] 至少 1 个仓库配置了 GitHub Actions
- [ ] 完整的 Markdown 知识库（覆盖 5 个阶段）
- [ ] 50+ 面试题 + 答案
- [ ] 至少 1 个公司项目实战案例（可内部分享）

### 软性能力

- [ ] 能在公司项目中独立设计并交付自动化测试方案
- [ ] 能讲清楚 POM、pytest fixture、Allure 集成原理
- [ ] 能用 Git + GitHub 协作（PR、Code Review）
- [ ] 求职面试时能自信讲解自己的测试框架项目

---

## 每日学习节奏建议

### 工作日（1-2 小时）

```
19:30 - 19:45    回顾昨日笔记（15min）
19:45 - 20:45    学习新内容（60min，看文档 + 写代码）
20:45 - 21:00    整理今日笔记（15min）
21:00 - 21:30    自由练习 / 提交代码到 GitHub（30min）
```

### 周末（4-6 小时）

```
上午 2h         阶段项目实战
下午 2-3h       项目实战 / 整理笔记 / 写博客
晚上 1h         总结本周 + 规划下周
```

### 番茄钟建议

- 一个番茄钟 25 分钟 + 5 分钟休息
- 每天完成 4-6 个番茄钟
- 周末完成 10-15 个番茄钟

---

## 后续可拓展方向（学完后可选）

| 方向 | 价值 | 难度 |
|------|------|------|
| **Playwright** | 现代 Web 自动化工具（您暂不需要，但可对比学习） | 中 |
| **Appium** | 移动端自动化 | 中 |
| **Locust** | 性能测试 | 中 |
| **pytest-bdd** | BDD 行为驱动开发 | 低 |
| **Docker** | 测试环境容器化 | 中 |
| **Jenkins** | 公司内部 CI/CD（GitHub Actions 之外的方案） | 中 |
| **测试平台开发** | Django/Flask + Vue 开发内部测试平台 | 高 |

---

## 立即开始：3 步上手

### 第 1 步：环境准备（今晚 30 分钟）

```bash
# 1. 安装 Python 3.10+（如有跳过）
python --version

# 2. 创建项目目录
mkdir D:\Pycode\auto-test-learning
cd D:\Pycode\auto-test-learning

# 3. 创建虚拟环境
python -m venv venv
.\venv\Scripts\Activate.ps1

# 4. 安装核心库
pip install pytest selenium webdriver-manager requests pyyaml allure-pytest loguru

# 5. 验证安装
pytest --version
python -c "import selenium; print(selenium.__version__)"
```

### 第 2 步：建立笔记仓库（今晚 30 分钟）

```bash
# 在 D:\Pycode\ 下
git init notes
mkdir notes/01-python-basics notes/02-pytest notes/03-selenium notes/04-requests notes/05-allure notes/06-cicd notes/07-interview

# 写第一个笔记
code notes/01-python-basics/python-quick-refresh.md
```

### 第 3 步：建立第一个 GitHub 仓库

1. GitHub 创建 `auto-test-learning` 仓库（私有即可）
2. 本地关联并推送第一个 commit
3. 之后每个阶段都提交到这个仓库

---

## 总结

这份计划的核心思想是：

> **"学以致用，边学边练；以终为始，目标驱动"**

13 周后，您将拥有：
- 📁 2 个可展示的开源项目
- 📚 一套完整的知识库
- 💼 在公司能直接落地的实战经验
- 🎯 求职加分的项目经验

**最关键的一步**：从今晚开始，按照"立即开始"的 3 步执行！

如果在学习过程中遇到具体问题（如某个库报错、POM 设计问题），随时来找我，我可以帮您 debug 或设计方案。

---

> **计划制定时间**：2026-06-28
> **计划版本**：v1.0
> **预计完成时间**：2026-09-30（13 周后）
