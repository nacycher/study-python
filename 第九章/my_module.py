author = 'sky'

def add(a,b):
    return a+b


def total(*a):
    """
    参数a:一个列表
    返回a中所有元素的平方和
    """
    result = 0
    for i in a:
        result = result + i**2
    return result

print(add(1,2))
print(total(1,2,3))