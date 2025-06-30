def f() :
    print("Hello World!")
f()

def sum(a, b) :
    print(a + b)
sum(1, 2)

def power(x, n = 2): # n = 2 是默认参数
    return x ** n
print(power(2, 2))
print(power(3))

int("16")
# int("16", 2)

def total(*args): # 可变参数，元组
    print(args)
    for i in args:
        print(i)

total(1, 2, 3, 4, 5)

def f(**kwargs): # 可变参数，字典
    for k, v in kwargs.items():
        print(k, v)

d = {"name":"小明", "age":18, "gender":"男"}
e = {"name1":"小明", "age1":18, "gender1":"男"}
f(**d, **e)

