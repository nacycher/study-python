# m行n列*号矩阵
m = 4
n = 5
for i in range(m):
    for j in range(n):
        print("*", end="")
    print()

# 打印n行的等腰三角形
n = 8
a = 1
b = n-1
for i in range(n):
    print(" "*b + "*"*a)
    a += 2
    b -= 1

'''
第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个
第二天早上又将剩下的桃子吃掉一半，又多吃了一个
第三天早上又将剩下的桃子吃掉一半，又多吃了一个
第四天只剩一个桃子
请问第一天共摘了多少个桃子
'''
peach = 1
while True:
    d1 = peach//2 -1
    d2 = d1//2 -1
    d3 = d2//2 -1
    if d3 == 1:
        print(peach)
        break
    peach += 1