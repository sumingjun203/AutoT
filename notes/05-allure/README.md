# 05 - Allure 测试报告

> Week 11 学习笔记
> 目标：生成专业可视化测试报告

---

## 📚 笔记列表

| Day | 主题 | 笔记 | 完成 |
|-----|------|------|------|
| Day 71 | Allure 安装与环境配置 | [day71-allure-install.md](./day71-allure-install.md) | ☐ |
| Day 72 | Allure 基础装饰器 | [day72-allure-decorators.md](./day72-allure-decorators.md) | ☐ |
| Day 73 | Allure 步骤与附件 | [day73-allure-steps-attach.md](./day73-allure-steps-attach.md) | ☐ |
| Day 74 | Allure 严重级别与 epic/feature/story | [day74-allure-severity.md](./day74-allure-severity.md) | ☐ |
| Day 75 | Allure 趋势图与历史 | [day75-allure-trend.md](./day75-allure-trend.md) | ☐ |
| Day 76 | Allure 与 Selenium/requests 集成 | [day76-allure-integration.md](./day76-allure-integration.md) | ☐ |
| Day 77 | Allure 报告美化 | [day77-allure-polish.md](./day77-allure-polish.md) | ☐ |
| Day 78 | Week 11 总结 | [day78-week-summary.md](./day78-week-summary.md) | ☐ |

## 🚀 速记表

| 速记表 | 内容 | 完成 |
|--------|------|------|
| Allure 装饰器速记 | [allure-decorators-cheatsheet.md](./allure-decorators-cheatsheet.md) | ☐ |

---

## 🎯 核心知识点

### 必会
- ✅ `@allure.title()` / `@allure.feature()` / `@allure.story()`
- ✅ `@allure.step()` 步骤拆解
- ✅ `allure.attach()` 附件（截图、日志、请求响应）
- ✅ `pytest --alluredir=./allure-results`
- ✅ `allure serve ./allure-results` 查看报告

### 进阶
- ⭐ `@allure.severity()` 严重级别
- ⭐ `@allure.epic()` 大模块划分
- ⭐ 历史趋势（allure-history）
- ⭐ 与 GitHub Pages 集成展示报告

---

## 📚 参考资源

- Allure 官方：https://allurereport.org/docs/
- allure-pytest：https://github.com/allure-framework/allure-python

---

**最后更新**：2026-06-28