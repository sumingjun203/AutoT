# 03 - Selenium Web 自动化

> Week 3-6 学习笔记
> 目标：掌握 Selenium + POM 设计模式

---

## 📅 Week 3-6 笔记

| Day | 主题 | 笔记 | 完成 |
|-----|------|------|------|
| Day 15 | 环境搭建（WebDriver、webdriver-manager） | [day15-environment.md](./day15-environment.md) | ☐ |
| Day 16 | 8 种元素定位方式 | [day16-locators.md](./day16-locators.md) | ☐ |
| Day 17 | 常用操作（点击/输入/获取属性） | [day17-basic-operations.md](./day17-basic-operations.md) | ☐ |
| Day 18 | 三种等待机制 | [day18-waits.md](./day18-waits.md) | ☐ |
| Day 19 | 高级交互（鼠标/键盘/iframe） | [day19-advanced-interactions.md](./day19-advanced-interactions.md) | ☐ |
| Day 20 | 弹窗与文件上传 | [day20-alerts-uploads.md](./day20-alerts-uploads.md) | ☐ |
| Day 21 | 截图与日志 | [day21-screenshots-logs.md](./day21-screenshots-logs.md) | ☐ |
| Day 22 | pytest + Selenium 整合 | [day22-pytest-selenium.md](./day22-pytest-selenium.md) | ☐ |
| Day 23 | conftest 与 driver fixture | [day23-conftest-driver.md](./day23-conftest-driver.md) | ☐ |
| Day 24 | POM 设计模式概念 | [day24-pom-concept.md](./day24-pom-concept.md) | ☐ |
| Day 25 | POM 实战：BasePage | [day25-base-page.md](./day25-base-page.md) | ☐ |
| Day 26 | 数据驱动（YAML） | [day26-data-driven.md](./day26-data-driven.md) | ☐ |
| Day 27 | saucedemo 项目实战 | [day27-saucedemo-project.md](./day27-saucedemo-project.md) | ☐ |
| Day 28 | Week 3-4 总结 | [day28-week-summary.md](./day28-week-summary.md) | ☐ |
| Day 29-35 | 公司项目实战 | [day29-35-company-project.md](./day29-35-company-project.md) | ☐ |

## 🚀 速记表（重点）

| 速记表 | 内容 | 完成 |
|--------|------|------|
| 元素定位速记 | [locator-cheatsheet.md](./locator-cheatsheet.md) | ☐ |
| 等待机制速记 | [waits-cheatsheet.md](./waits-cheatsheet.md) | ☐ |
| POM 设计模式总结 | [pom-design-pattern.md](./pom-design-pattern.md) | ☐ |
| 常见报错解决方案 | [troubleshooting.md](./troubleshooting.md) | ☐ |

---

## 🎯 核心知识点

### 必会
- ✅ 8 种元素定位（重点：xpath、css_selector）
- ✅ 三种等待（implicit / explicit / sleep）
- ✅ iframe 切换、alert 处理
- ✅ POM 三层架构（pages / tests / utils）
- ✅ BasePage 公共方法封装

### 进阶
- ⭐ 自定义 expected_conditions
- ⭐ 失败自动截图 + page source
- ⭐ 日志集成（loguru）
- ⭐ 多浏览器并行测试
- ⭐ 无头模式 / 禁用图片

---

## 📚 参考资源

- Selenium Python：https://selenium-python.readthedocs.io/
- Selenium 官方：https://www.selenium.dev/documentation/
- webdriver-manager：https://github.com/SergeyPirogov/webdriver_manager

### 练习网站
- https://www.saucedemo.com/ — 经典练习场
- https://the-internet.herokuapp.com/ — 综合场景
- https://practice.expandtesting.com/ — 多种场景

---

**最后更新**：2026-06-28