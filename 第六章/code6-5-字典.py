# 字典的创建
d = {
    "name" : "lb",
    "gender" : True,
    "name" : 'lb2' # 建重复的话，会覆盖之前的值
}
print(d)
print(type(d))
# 新增键值对
d['height'] = 170
print(d)
# 获取键值对
name = d['name']
print(name)
# 修改键值对
d['height'] = 173
# 字典的遍历
for k, v in d.items():
    print(k, v)
for k in d.keys():
    print(k)
for v in d.values():
    print(v)
# 字典的常用方法
d.pop('name')
print(d)