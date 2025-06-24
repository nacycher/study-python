print(list(range(10)))
print(list(range(2,10)))
print(list(range(2,10,3)))

# 高斯求和
total = 0
for i in range(10):
    total += i
print(total)

# 水仙花数，每数字的立方和等于这个数本身
for i in range(100, 1000):
    # a = i // 100
    # b = (i % 100) // 10
    # c = i % 10
    t = str(i) # 将int转换为str，123 -> "123"
    a = int(t[0])
    b = int(t[1])
    c = int(t[2])
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
