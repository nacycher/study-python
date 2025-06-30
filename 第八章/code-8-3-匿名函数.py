from functools import reduce


def sum(a, b):
    return a + b

print(sum(1, 2))

# 匿名函数
result = lambda a,b:a+b
print(result(1, 2))

# map函数处理列表a
a = [1, 2, 3, 4, 5]
result = map(lambda x:x**2, a)
print(list(result))

# reduce 累积
result = reduce(lambda  x,y:x*y, a)
print(result)

# filter 过滤
result = filter(lambda x:x%2==0, a)
print(list(result))
