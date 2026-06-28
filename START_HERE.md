# 🚀 START HERE — 13 周学习路线入门指引

> 不知道从哪里开始？读完这一页，跟着做就行。

---

## 📅 第一步：今晚 30 分钟 — 环境验证

### 1.1 激活虚拟环境

```powershell
cd H:\Code\AutoT
.\.venv\Scripts\Activate.ps1
```

### 1.2 安装核心库

```powershell
pip install pytest selenium webdriver-manager requests pyyaml allure-pytest loguru
```

### 1.3 验证安装

```powershell
pytest --version
python -c "import selenium; print('selenium', selenium.__version__)"
python -c "import requests; print('requests', requests.__version__)"
```

✅ 如果三行命令都成功打印版本号，说明环境就绪！

---

## 📅 第二步：明天起 — 按周推进

### Week 1-2：Python 速成 + pytest 入门

**Day 1 任务清单**（今晚 1.5h）：

- [ ] 打开 Python 官方文档：https://docs.python.org/zh-cn/3/tutorial/
- [ ] 学习变量、数据类型、字符串格式化（f-string）
- [ ] 写 10 个字符串处理函数练习（保存到 `notes/01-python-basics/exercises/`）
- [ ] 整理笔记到 `notes/01-python-basics/day01-variables-and-strings.md`

**Week 1 学习路径**：

| Day | 主题 | 笔记文件 |
|-----|------|---------|
| Day 1 | 变量、字符串 | `notes/01-python-basics/day01-variables-and-strings.md` |
| Day 2 | 控制流 | `notes/01-python-basics/day02-control-flow.md` |
| Day 3 | 函数 | `notes/01-python-basics/day03-functions.md` |
| Day 4 | 数据结构 | `notes/01-python-basics/day04-data-structures.md` |
| Day 5 | 类与对象 | `notes/01-python-basics/day05-classes.md` |
| Day 6-7 | 综合复习 | `notes/01-python-basics/week01-summary.md` |

**Week 1 实战**：用 Python 写一个 **Todo List 命令行小工具**（存放在 `projects/_sandbox/`）

---

## 📅 第三步：每天的时间分配

### 工作日（1.5h / 天）

```
19:30 - 19:45    回顾昨日笔记（15min）
19:45 - 20:45    学习新内容（60min，看文档 + 写代码）
20:45 - 21:00    整理今日笔记（15min）
21:00 - 21:30    自由练习 / 提交代码到 GitHub（30min）
```

### 周末（5h / 天）

```
上午 2h         阶段项目实战
下午 2-3h       项目实战 / 整理笔记 / 写博客
晚上 1h         总结本周 + 规划下周
```

---

## 📅 第四步：每个阶段的产出节奏

| 周次 | 阶段产出 | 验收标准 |
|------|---------|---------|
| Week 2 结束 | calculator 项目 | 10+ 用例、3 个 parametrize、2 个 fixture |
| Week 6 结束 | saucedemo-demo | 15+ 用例、POM 完整、数据驱动 |
| Week 10 结束 | api-test-demo | 20+ 用例、鉴权完整、接口关联 |
| Week 12 结束 | CI/CD + Allure | GitHub Actions 自动跑测、报告可视化 |
| Week 13 结束 | 作品集 | 2 个公开仓库 + 50 面试题 |

---

## 🎯 关键里程碑

每完成一个里程碑，给自己一个奖励 🎉：

- [ ] 🎁 **Milestone 1**（Week 2）：第一个 pytest 项目跑通
- [ ] 🎁 **Milestone 2**（Week 6）：第一个 Selenium + POM 框架完成
- [ ] 🎁 **Milestone 3**（Week 10）：第一个完整 API 框架在公司能用
- [ ] 🎁 **Milestone 4**（Week 12）：GitHub Actions 自动跑测上线
- [ ] 🎁 **Milestone 5**（Week 13）：作品集上线，更新简历

---

## 🆘 遇到问题怎么办？

按这个优先级解决：

1. **官方文档** —— pytest / Selenium / requests 官方文档第一手
2. **搜索引擎** —— 把报错信息原样搜索
3. **GitHub Issues** —— 搜相关项目的 issue
4. **AI 助手** —— 描述清楚问题 + 贴代码 + 贴报错
5. **测试工程师社区** —— TesterHome、思寒Tester

---

## 📌 一些容易踩的坑

### ❌ 不要追求完美

> "学完所有知识再开始写代码" 是最大的陷阱。
> 边学边练，**用项目驱动学习**。

### ❌ 不要只看不练

> 看视频/文档时手要动，**每学一个知识点就写一个小 demo**。

### ❌ 不要陷入环境配置

> Selenium 驱动问题用 `webdriver-manager` 自动管理。
> 不要花超过 1 小时在环境配置上。

### ✅ 要每天写笔记

> 笔记不是给别人看的，**是给自己复习用的**。
> 推荐用 Markdown，方便搜索。

### ✅ 要给代码加注释

> 一周后你看自己的代码会像看别人的代码一样陌生。
> 注释 = 未来的你写给现在你的信。

---

## 🎓 第一天具体行动计划

如果今天是 Day 1，您应该：

### ⏰ 19:30 - 19:45（15min）环境准备

```powershell
cd H:\Code\AutoT
.\.venv\Scripts\Activate.ps1
python --version
```

### ⏰ 19:45 - 20:45（60min）学习 + 练习

1. 阅读 Python 官方文档"3.1.1. 数字"、"3.1.2. 字符串"、"3.1.3. 列表"
2. 动手写以下练习（保存到 `notes/01-python-basics/exercises/`）：

```python
# exercise_01.py
# 字符串处理练习

def reverse_string(s):
    """反转字符串"""
    return s[::-1]

def is_palindrome(s):
    """判断是否为回文"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_vowels(s):
    """统计元音字母个数"""
    return sum(1 for c in s.lower() if c in "aeiou")

# 测试
if __name__ == "__main__":
    print(reverse_string("hello"))        # olleh
    print(is_palindrome("A man a plan a canal Panama"))  # True
    print(count_vowels("Hello World"))    # 3
```

### ⏰ 20:45 - 21:00（15min）整理笔记

创建 `notes/01-python-basics/day01-variables-and-strings.md`：

```markdown
# Day 01 - 变量与字符串

## 学到的内容
- Python 变量无需声明类型
- 字符串是不可变对象
- f-string 是格式化字符串的最佳方式

## 关键代码片段
...

## 今日练习
- exercise_01: 字符串反转
- exercise_02: 回文判断
- exercise_03: 元音统计

## 明日计划
- 控制流：if/else、for、while
```

### ⏰ 21:00 - 21:30（30min）提交到 Git

```powershell
git add .
git commit -m "Day 01: Python 字符串基础"
```

---

## ✅ 每日结束检查清单

完成一天的学习后，问自己：

- [ ] 今天至少写了 50 行代码吗？
- [ ] 今天整理了笔记吗？
- [ ] 今天有 commit 吗？
- [ ] 明天的任务清晰吗？

如果 4 个都是 ✅，今天就是成功的一天！

---

## 🚀 现在开始！

关掉这个文件，打开 `notes/01-python-basics/` 文件夹，开始 Day 1！

> **记住：开始 > 完美**

---

**最后更新**：2026-06-28