# 题目要求，输入2025-02-25，计算这一天数这一年的第几天
date = input("请输入日期（格式：yyyy-mm-dd）：").split("-")
year = int(date[0])
month = int(date[1])
day = int(date[2])
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(sum(days))

result = 0
for i in range(month):
    result += days[i]
result += day
print("这一天是这一年的第", result, "天")
