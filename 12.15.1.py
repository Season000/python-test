# 列表的相关测试
list = [1,2,3,4,5]
for i in range(len(list)):
    print(i)
list1 = [6,7]
list.extend(list1)
list.extend(['this is a list'])
print(list)
# list.remove(list[-1])
# del list[-1]
temp = list.pop()
print(list)
print(temp)
print(list[0:-1]) # 切片
print(list[:-2])
temp = list[:] # 列表的拷贝
print(temp)

 # 列表的比较
list1 = [123]
list2 = [234]
print(list1>list2) # false

list1 = [123,456]
list2 = [234,123]
print(list1>list2) # false
print(list1<list2) # true 从第一位开始判断
# list3 = list1 + list2
list3 = []
list3.extend(list2 + list1)
print(list3)

list = [123,[135,678],234,345] # 列表元素为列表
print(135 in list[1])

