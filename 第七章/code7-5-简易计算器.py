while True:
    try:
        op = input("请输入一个四则运算式（例如1+2）：")
        if '+' in op:
            a = int(op.split('+')[0])
            b = int(op.split('+')[1])
            print(a + b)
            continue
        elif '-' in op:
            a = int(op.split('-')[0])
            b = int(op.split('-')[1])
            print(a - b)
            continue
        elif '*' in op:
            a = int(op.split('*')[0])
            b = int(op.split('*')[1])
            print(a * b)
            continue
        elif '/' in op:
            a = int(op.split('/')[0])
            b = int(op.split('/')[1])
            print(a / b)
            continue
        elif 'c' == op:
            print("退出")
            break
        else:
            raise Exception("输入错误,请重新输入")
    except ZeroDivisionError:
        print("除数不能为0")
        continue
    except Exception as e:
        print(e)
        continue