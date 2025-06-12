# and
print(True and False)
print(True and True)
print(True and False and True)
print(1==1 and True and 2<3)
# ’‘是False，其他有值的字符串是True
# and 会返回第一个为False的值，如果都为True，返回最后一个值
# or 会返回第一个为True的值，如果都为False，返回最后一个值
# 这里适用与一些兜底数据，默认值
print('hello' and 'hi')
print('' and 'hi')
print(0 and 'hi')

# or
print(True or False)
print(2024 or 2025)
print(0 or '888')

# not
print(not True)
print(not 1)
print(not 'hello')

# 优先级 not > and > or
print(True and not False)