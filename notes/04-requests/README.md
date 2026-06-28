# 04 - requests API 自动化

> Week 7-10 学习笔记
> 目标：掌握 requests + pytest API 测试框架

---

## 📅 Week 7-10 笔记

| Day | 主题 | 笔记 | 完成 |
|-----|------|------|------|
| Day 43 | HTTP 协议基础回顾 | [day43-http-basics.md](./day43-http-basics.md) | ☐ |
| Day 44 | requests 基础（get/post/put/delete） | [day44-requests-basics.md](./day44-requests-basics.md) | ☐ |
| Day 45 | 响应处理（status/json/headers） | [day45-response-handling.md](./day45-response-handling.md) | ☐ |
| Day 46 | Session 与 Cookie | [day46-session-cookie.md](./day46-session-cookie.md) | ☐ |
| Day 47 | 鉴权处理（Token/JWT/Basic） | [day47-authentication.md](./day47-authentication.md) | ☐ |
| Day 48 | 文件上传下载 | [day48-file-operations.md](./day48-file-operations.md) | ☐ |
| Day 49 | API 框架设计（分层） | [day49-api-framework.md](./day49-api-framework.md) | ☐ |
| Day 50 | API 封装层（base_api） | [day50-api-wrapper.md](./day50-api-wrapper.md) | ☐ |
| Day 51 | 数据驱动（YAML/JSON） | [day51-data-driven.md](./day51-data-driven.md) | ☐ |
| Day 52 | 接口关联（jsonpath/正则） | [day52-api-chaining.md](./day52-api-chaining.md) | ☐ |
| Day 53 | fixture 进阶 | [day53-fixture-advanced.md](./day53-fixture-advanced.md) | ☐ |
| Day 54 | unittest.mock 入门 | [day54-mock-basics.md](./day54-mock-basics.md) | ☐ |
| Day 55 | responses Mock HTTP | [day55-responses-mock.md](./day55-responses-mock.md) | ☐ |
| Day 56 | api-test-demo 项目实战 | [day56-api-test-demo.md](./day56-api-test-demo.md) | ☐ |
| Day 57-70 | 公司项目 API 实战 | [day57-70-company-api.md](./day57-70-company-api.md) | ☐ |

## 🚀 速记表

| 速记表 | 内容 | 完成 |
|--------|------|------|
| requests 常用方法 | [requests-cheatsheet.md](./requests-cheatsheet.md) | ☐ |
| HTTP 状态码 | [http-status-codes.md](./http-status-codes.md) | ☐ |
| 鉴权方式速记 | [auth-cheatsheet.md](./auth-cheatsheet.md) | ☐ |
| 常见报错解决方案 | [troubleshooting.md](./troubleshooting.md) | ☐ |

---

## 🎯 核心知识点

### 必会
- ✅ GET / POST / PUT / DELETE 区别
- ✅ params / data / json 传参区别
- ✅ Session 跨请求保持 Cookie
- ✅ 鉴权：Bearer Token / Basic Auth / JWT
- ✅ 文件上传（files 参数）
- ✅ 接口关联（响应提取 + 注入）

### 进阶
- ⭐ JSON Schema 校验
- ⭐ unittest.mock patch
- ⭐ responses 库 Mock HTTP
- ⭐ pymysql 验证接口落库
- ⭐ HTTPS / 代理 / 超时重试

---

## 📚 参考资源

- requests 官方：https://requests.readthedocs.io/zh_CN/latest/
- HTTP 协议：https://developer.mozilla.org/zh-CN/docs/Web/HTTP
- jsonpath：https://goessner.net/articles/JsonPath/

### 练习 API
- https://httpbin.org/ — 通用测试
- https://reqres.in/ — 真实场景模拟
- 公司测试环境 API

---

**最后更新**：2026-06-28