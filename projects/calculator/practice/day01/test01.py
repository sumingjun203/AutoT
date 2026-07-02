#1. 变量交换
# 不使用第三个变量，交换 `a = 10`、`b = 20` 的值，并打印交换前后结果。

def swag():
  a=10
  b=20
  print(f'交换前,{a=},{b=}')
  a,b=b,a
  print(f'交换后,{a=},{b=}')


#### 2. 类型识别器
# 编写函数 `describe(value)`，根据输入返回字符串：
# - `int` → `"整数: <值>"`
# - `float` → `"浮点: <值>，保留 2 位 = <值:.2f>"`
# - `str` → `"字符串: '<值>'，长度=<len>"`
# - `bool` → `"布尔: <值>"`
# - `None` → `"空值"`
# - 其他 → `"未知类型: <类型名>"`

'''
print(describe(42))         # 整数: 42
print(describe(3.14159))    # 浮点: 3.14159，保留 2 位 = 3.14
print(describe("hi"))       # 字符串: 'hi'，长度=2
print(describe(True))       # 布尔: True
print(describe(None))       # 空值
'''

def describe(value) -> None:
  if type(value) is int:
   print(f'整数：{value}')
  elif type(value) is float:
    print(f'浮点：{value},保留2位={value:.2f}')
  elif type(value) is str:
    print(f'字符串：\'{value}\',长度={len(value)}')
  elif type(value) is bool:
    print(f'布尔：{value}')
  elif type(value) is None:
    print(f'"空值"')
  elif type(value) is not bool or type(value) is not str or type(value) is not int or type(value) is not float or type(value) is not None:
    print(f'未知类型:{type(value)}')
  
# if __name__=='__main__':
#   describe(121)
#   describe(121.123132)
#   describe('121.123132')
#   describe(True)
#   describe(None)

#### 3. 温度转换器
# 编写函数 `celsius_to_fahrenheit(c)`，公式：`F = C × 9/5 + 32`。要求：
# - 如果传入非数字（`int`/`float`），抛 `TypeError`
# - 用 f-string 输出 `"{c}°C = {f}°F"`，保留 1 位小数
def celsius_to_fahrenheit(c) -> None :
  assert c is not int,'TypeError'
  assert c is not float,'TypeError'
  f = (c * 9 / 5) + 32
  print(f'"{c}°C = {f:.1f}°F"')
  
# if __name__ == '__main__':
#   celsius_to_fahrenheit('10')
#



#### 4. 字符串工具箱
# 封装 5 个常用字符串工具函数（自动化测试必备）：
def normalize(text: str) -> str:
    """去首尾空格 + 转小写"""
    return str.strip(text).lower()
    
def is_chinese_phone(phone: str) -> bool:
  """判断是否为中国大陆手机号（11 位，1 开头）"""
  if not phone.startswith('1'):
    return False
  elif len(phone) != 11:
    return False
  else:
    return True


def mask_email(email: str) -> str:
  """把邮箱用户名部分第 2 位之后替换为 *，例如 alice@x.com → a***e@x.com"""
  new_strlist=email.split('@')
  new_user=new_strlist[0]
  for i in range(0,len(new_strlist[0])):
    if i >=1:
      new_user=new_user.replace(new_user[i],'*')
  new_strlist[0]=new_user
  return ''.join(new_strlist)
  
  
def truncate(text: str, max_len: int = 20, suffix: str = "...") -> str:
  """超过 max_len 则截断并加 suffix"""
  if len(text) <= max_len:
    return text
  else:
    return text[:max_len] + suffix

def extract_digits(text: str) -> str:
  """从字符串中提取所有数字，例如 '订单 ABC123 已发货' → '123'"""
  number=''
  for i in text:
    if i.isdigit():
      number += i
  return number


#### 5. 身份证信息提取（自动化测试中的典型场景）
# 编写函数 `parse_id_card(id_card: str) -> dict`，从 18 位身份证号中提取：
# - `birthday`：格式 `"YYYY-MM-DD"`（第 7-14 位）
# - `gender`：`"男"` 或 `"女"`（第 17 位：奇男偶女）
# - `region_code`：前 6 位
#
# 调用示例：
# ```python
# print(parse_id_card("110101199003078811"))
# {'birthday': '1990-03-07', 'gender': '男', 'region_code': '110101'}
# 说明：身份证第 17 位（索引 16）是 '1'（奇数），按"奇男偶女"规则 → 男
# 速算小窍门：直接看第 17 位，1/3/5/7/9 → 男，0/2/4/6/8 → 女
def parse_id_card(id_card: str) -> dict:
  assert len(id_card) != 18,print(f'身份证不是18位')
  if id_card.isdigit()==False and id_card[17]!='X':
    print(f'不是身份证')
    return {}
  dict_card={}
  region_code=id_card[0:6]
  birthday=id_card[6:10]+'-'+id_card[10:12]+'-'+id_card[12:14]
  if int(id_card[16]%2!=0):
    gender='男'
  else:
    gender='女'
  dict_card['region_code']=region_code
  dict_card['birthday']=birthday
  dict_card['gender']=gender
  return dict_card

#### 6. 测试报告生成器
# 编写函数 `format_report(results: list[dict]) -> str`，输入形如：
# ```python
# results = [
#     {"name": "登录成功", "status": "PASS", "duration": 0.123},result[1]
#     {"name": "查询订单", "status": "PASS", "duration": 0.456},result[2]
#     {"name": "删除订单", "status": "FAIL", "duration": 0.089},result[3]
#     {"name": "退出登录", "status": "PASS", "duration": 0.012},result[4]
# ]
# ```
# 输出对齐的报告（用 f-string 格式化，宽度自定义）：
# ```
# 用例名称        状态     耗时(s)
# ----------  --------  --------
# 登录成功       PASS     0.123
# 查询订单       PASS     0.456
# 删除订单       FAIL     0.089
# 退出登录       PASS     0.012
# ----------  --------  --------
# 通过: 3  失败: 1  总计: 4
# ```
def format_report(results: list[dict]) -> str:
  result=f''
  
  
  return result

















