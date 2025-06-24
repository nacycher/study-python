# 列表创建
list1 = []
print(list1)
print(type(list1))
list2 = [1, 2, 3, True, 'hello']
print(list2)
list3 = list("12345678")
print(list3)
# 列表的索引
print(list3[1])
# 列表的切片, 从下标为2的元素开始，到下标为6的元素结束，步长为2
print(list3[2:6:2])
# 列表的乘法和加法
print(list3 + list2)
print(list3 * 3)
# 列表的成员运算
print('1' in list3)
print('1,2,3' in list3)
# 列表的函数
print(len(list3))
print(max(list3))
print(min(list3))
# del list3


print('-' * 20)

# 列表的遍历
for i in list2:
    print(i)
for i,j in enumerate(list2):
    print(i,j)
for i in range(len(list2)):
    print(i, list2[i])

# 列表的常用方法
# 添加元素
list3.append('666')
print(list3)
list3.extend(list2)
print(list3)
list3.insert(1,'777')
print(list3)
# 根据索引删除元素
list3.pop(1)
print(list3)
list3.remove('666')
print(list3)
# 清空列表
list.clear(list2)

# 计算若干个人的平均年龄
age = [10, 20, 30, 40, 23, 45]
print(sum(age) / len(age))