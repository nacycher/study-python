# 浮点数的计算
n1 = 0.1
n2 = 0.2
# 计算精度有误差
print(n1 + n2)

# 四舍五入函数：round
n3 = round(n1 + n2, 2)
print(n3)

import math
n1 = 2.1
n2 = 15.256
# 向上取整： ceil
n4 = math.ceil(n1 + n2)
print(n4)
# 向下取整: floor
n5 = math.floor(n1 + n2)
print(n5)
