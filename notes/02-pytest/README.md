# 02 - pytest 入门到精通

> Week 1-2 重点，Week 3+ 持续深入
> 目标：掌握 pytest 全部核心功能

---

## 📚 笔记列表

### Week 1-2 入门笔记
- 见 [01-python-basics/README.md](../01-python-basics/README.md) Day 8-14

### Week 3+ 进阶笔记（待创建）

| 主题 | 笔记 | 完成 |
|------|------|------|
| fixture 进阶（scope、autouse、嵌套） | [fixture-advanced.md](./fixture-advanced.md) | ☐ |
| 标记（mark）：skip、xfail、custom | [marks.md](./marks.md) | ☐ |
| 配置文件 pytest.ini / pyproject.toml | [configuration.md](./configuration.md) | ☐ |
| 插件生态（rerunfailures、xdist、order） | [plugins.md](./plugins.md) | ☐ |
| 常用命令行参数速查 | [cli-cheatsheet.md](./cli-cheatsheet.md) | ☐ |

---

## 🎯 核心知识点

### 必会
- ✅ `assert` 断言 + 失败信息解读
- ✅ `@pytest.mark.parametrize` 参数化
- ✅ `@pytest.fixture` + scope
- ✅ `conftest.py` 分层共享
- ✅ pytest.ini 配置（testpaths、markers）

### 进阶
- ⭐ fixture 嵌套与 factory as fixture
- ⭐ `pytest --maxfail=N -x -v -k` 命令行
- ⭐ 自定义 mark 与 `-m` 过滤
- ⭐ 失败重试（pytest-rerunfailures）
- ⭐ 并发执行（pytest-xdist）

---

## 📚 参考资源

- pytest 官方：https://docs.pytest.org/en/stable/
- pytest 插件列表：https://docs.pytest.org/en/stable/reference/plugin_list.html

---

**最后更新**：2026-06-28