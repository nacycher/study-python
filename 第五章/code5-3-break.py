while True:
    print("-" * 10)
    break

while True:
    name = input("请输入你的名字：")
    if name == "lb":
        print("欢迎回家")
        break
    else:
        print("不在家")

for i in range(10):
    if i > 0 and i % 3 == 0:
        print(i)
        break

# 判断一个数是否为质数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        i += 1
    return True

print("2是不是质数:", is_prime(2))
print("3是不是质数:", is_prime(3))
print("4是不是质数:", is_prime(4))
print("5是不是质数:", is_prime(5))
print("10是不是质数:", is_prime(10))
