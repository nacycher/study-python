# 用户名，密码，黑名单
users = [
    {
        'name': 'lb',
        'pws': '123456',
        'status': True
    },
    {
        'name': 'zs',
        'pws': '1236',
        'status': True
    },
    {
        'name': 'ls',
        'pws': '12345678',
        'status': False
    }
]
print(users)
flag = False
for i in range(3):
    user = input("请输入用户名：")
    pws = input("请输入密码：")
    for u in users:
        if u['name'] == user:
            if u['pws'] == pws:
                if u['status']:
                    print("登录成功")
                    flag = True
                    break
                else:
                    print("账户已被锁定")
            else:
                print("密码错误")
            break
    else:
        print("用户名不存在")
    if flag:
        break