age = input("请输入你的年龄：")
if age.isdigit():
    age = int(age)
    if 0 <= age <= 120:
        print("输入正确")
    else:
        print("输入错误")