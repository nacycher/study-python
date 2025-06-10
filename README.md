# study-python
study-python

# 目录
- [第一个程序](#第一个程序)
- [变量](#变量)

# 简介
章节：
![img.png](images/py-01-01.png)
![img_1.png](images/py-01-02.png)

# 第一个程序
```python
# 打印数字
print(2024)

# 打印字符串
print("hello world")

print(333)
```
## 注释
```python
# 块注释
# 我是块注释
print(111)

# 行内注释
print(222) #我是块注释

# 多行注释
'''
我是多行注释
'''
print(333)
```

## 打印变量
```python
# 任务3：创建变量year值为2024
year = 2024
print(year)
```

## 一行打印多个内容
```python
print("我是main")
year = 2024
# sep，分隔符，设置打印多个内容的分隔符，默认值是一个空格
print(year, "年，我要减肥", sep="")
print(year, "年，我要旅游", sep="")
print(year, "年，我要学习", sep="")
# end，打印完后，自动追加的内容，默认是\n换行
print(end="*")
```

## 格式化输出
```python
month = 2
day = 20
week = "一"
weather = "晴"
temp = 19.5
year = 2025

# %d整形，%s字符型，%f浮点型
# %2d表示占2位， %02d表示占2位，不够使用0填充
# %.2f 表示小数点2位
print("今天是%d年%02d月%d日，星期%s, 天气%s，温度%.2f" % (year, month, day, week, weather, temp))
```

## input的使用
```python
month = 2
day = 20
week = "一"
weather = "晴"
temp = 19.5
year = 2025

# %d整形，%s字符型，%f浮点型
# %2d表示占2位， %02d表示占2位，不够使用0填充
# %.2f 表示小数点2位
print("今天是%d年%02d月%d日，星期%s, 天气%s，温度%.2f" % (year, month, day, week, weather, temp))
```

## 流程图
![img.png](images/py-12-02.png)
![img_1.png](images/py-12-01.png)

## 章末总结
![img.png](images/py-13-01.png)

# 变量
## 变量的创建
创建单个，多个变量
![img.png](images/py-15-01.png)
![img.png](images/py-15-02.png)
```pycon
# 任务：买苹果
price = 10.5
weight = 7.5
money = price * weight
print("总共消费了%.2f" % money)
```
## 变量的修改
```python
# year = 2023
# print(year)
# year = 2024
# print(year)
#
# # 正确执行,不同类型的变量可以相互赋值
# money = '10元'
# money = 10
# print(money)

# 超市打折活动
price = 10.5
weight = 7.5
money = price * weight
money = money - 5
print("总共消费了%.2f" % money)
```

## 变量的命名
python使用大写表示常量
![img.png](images/py-17-01.png)
- 见名知义
- 不能使用关键字
- 不能使用数字开头
- 驼峰命名法

## 变量的类型
```python
a = 'afd'
print(type(a))
print(isinstance(a, str))
print(isinstance(a, int))
print(isinstance(a, float))
```
![img.png](images/py-18-01.png)