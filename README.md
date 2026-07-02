# Python 自动化测试学习项目

> 13 周从零到能独立交付自动化测试框架
> 个人学习笔记 + 实战项目 + 作品集

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-8.x-green.svg)](https://docs.pytest.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-orange.svg)](https://selenium-python.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📂 项目结构

```
H:\Code\AutoT\
├── .omo/                          # 学习计划与草稿
│   ├── plans/                     # 学习计划文件
│   └── drafts/                    # 访谈草稿
├── notes/                         # 学习笔记（Markdown）
│   ├── 01-python-basics/          # Python 语法速记
│   ├── 02-pytest/                 # pytest 笔记
│   ├── 03-selenium/               # Selenium 笔记
│   ├── 04-requests/               # requests 笔记
│   ├── 05-allure/                 # Allure 报告
│   ├── 06-cicd/                   # CI/CD 笔记
│   ├── 07-interview/              # 面试题
│   └── 08-mindmap/                # 知识图谱
├── projects/                      # 实战项目
│   ├── calculator/                # 阶段一：pytest 单元测试
│   ├── saucedemo-demo/            # 阶段二：Selenium + POM
│   └── api-test-demo/             # 阶段三：requests + pytest
├── START_HERE.md                  # 👈 新手从这里开始
├── .gitignore
└── README.md                      # 本文件
```

---

## 🎯 学习目标

完成 13 周学习后，您将能够：

1. ✅ 独立搭建 pytest 测试项目（含 conftest、fixture、参数化）
2. ✅ 用 Selenium + POM 设计 Web UI 自动化框架
3. ✅ 用 requests 设计 API 自动化框架（含鉴权、数据驱动、Mock）
4. ✅ 集成 Allure 生成专业测试报告
5. ✅ 用 GitHub Actions 实现 CI/CD 自动跑测试
6. ✅ 在 GitHub 上展示 2 个完整可运行的开源测试项目

---

## 📅 5 阶段路线图

| 阶段 | 周次 | 内容 | 产出 |
|------|------|------|------|
| 一 | Week 1-2 | Python 速成 + pytest 入门 | calculator 项目 |
| 二 | Week 3-6 | Selenium Web UI 自动化 | saucedemo-demo |
| 三 | Week 7-10 | requests API 自动化 | api-test-demo |
| 四 | Week 11-12 | Allure 报告 + CI/CD | GitHub Actions 配置 |
| 五 | Week 13 | 作品集 + 知识沉淀 | 完整 README + 50 面试题 |

详细计划见：[`.omo/plans/python-auto-test-learning-plan.md`](.omo/plans/python-auto-test-learning-plan.md)

---

## 🚀 快速开始

```bash
# 1. 进入项目目录
cd H:\Code\AutoT

# 2. 激活虚拟环境（如果未激活）
.\.venv\Scripts\Activate.ps1

# 3. 安装核心依赖
pip install pytest selenium webdriver-manager requests pyyaml allure-pytest loguru

# 4. 阅读入门指引
code START_HERE.md
```

---

## 📊 学习进度跟踪

- [ ] 阶段一：Python 速成 + pytest 入门
- [ ] 阶段二：Selenium Web UI 自动化
- [ ] 阶段三：requests API 自动化
- [ ] 阶段四：Allure 报告 + CI/CD 整合
- [ ] 阶段五：作品集 + 知识沉淀

---

## 📚 推荐资源

- 详细计划：[`.omo/plans/`](.omo/plans/)
- 学习笔记：[`notes/`](notes/)
- 实战项目：[`projects/`](projects/)

---

## 📝 学习原则

> **每天 1.5h + 周末 5h，13 周不间断。**
> 比"突击学完"更重要的是"持续推进"。
