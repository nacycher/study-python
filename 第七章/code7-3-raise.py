try:
    pwd = input("请输入你的密码：")
    if len(pwd) < 8:
        raise Exception("密码长度不够")
except Exception as e:
    print(e)