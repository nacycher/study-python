# 全局变量
num1 = 10

# 局部变量
def test():
    global num1 # 声明使用的变量是全局变量
    num2 = 20
    num1 = 20 # 局部变量
    print(num1)
    print(num2)

test()

print("全局变量num1：", num1)