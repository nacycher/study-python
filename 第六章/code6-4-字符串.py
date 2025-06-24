s1 = 'hello world'

# 序列的通用操作
print(s1 + ' mia')
print(s1*3)
print(len(s1))
print('h' in s1)
# 遍历
for i in s1:
    print(i)
for index, value in enumerate(s1):
    print(index, value)
# 类型转换
print(list(s1))
print(tuple(s1))
print(set(s1))
# 字符串函数
# print(s1.strip())
print(s1.split(" "))
print("#".join(s1))