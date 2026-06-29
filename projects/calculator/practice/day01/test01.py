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
  
if __name__ == '__main__':
  celsius_to_fahrenheit('10')
  



