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

list = [123,[135,678],234,345,123] # 列表元素为列表
print(135 in list[1])

print(list.count(123)) # 计算123在list中出现了多少次

print(list.index(123)) # 列出123元素在列表中第一次出现的索引下标
print(list.index(123,2,7)) # 在list列表中2-7下标中索引第一次出现的

# reverse  列表翻转
list = [2,1,3,5,4,6,8,7]
list.reverse()# 翻转列表，原列表会变化
print(list)

# sort 列表排序
list.sort()  # 先从小到大排序，再翻转，就是从大到小排序了
list.reverse()
print(list)

# sort(func,key)
# sort(reverse) 默认为false
list.sort(reverse=True) # 倒序排序
print(list)