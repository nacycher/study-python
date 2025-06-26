try:
    print("有可能出现错误的代码")
    print(1 + '1')
except:
    print("如果出现错误，执行这里的代码")

try:
    n = int(input("请输入一个数字："))
    n = 5 / n
    print(n)
except ZeroDivisionError:
    print("除数不能为0")
except:
    print("输入的数字有误")