# 纸的厚度
n = 0.1
w = n
for i in range(50):
    w *= 2
    print(w)

# 国王熟麦粒
# 1-1 2-2 3-4 4-8..
g = 1 # 当前格子的麦粒数
total = 0 # 麦粒总数
a = 1 # 当前格子的序号
while a <= 100:
    total += g
    g *= 2
    a += 1
    print(total)

