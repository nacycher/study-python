# 10阶台阶，每次上1阶或2阶，有多少种走法
# 3阶：3种，111，12，21
# f(n) = f(n-1) + f(n-2)
def f(n): # 计算出n阶楼梯有多少种走法
    if n <= 2:
        return n
    return f(n-1) + f(n-2)

print(f(3))
print(f(10))