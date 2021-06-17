# 匿名函数练习

list2 = [{"name1": 18, "name2": 10}, {"name1": 13, "name2": 20}, {"name1": 9, "name2": 29}]

m = max(list2, key=lambda x: x['name1'])
print(m)

list1 = [3, 5, 8, 9, 2]
result = map(lambda x: x+2, list1)
print(list(result))

list3 = [12, 6, 8, 98, 34, 36, 2, 8, 0]

res = filter(lambda x: x > 10, list3)
print(list(res))


students = [
    {"name":"name1", "age":20},
    {"name":"name2", "age":19},
    {"name":"name3", "age":13},
    {"name":"name4", "age":23},
    {"name":"name5", "age":21}

]
# 取出所有年龄大于20的
result = filter(lambda x: x.get('age') > 20, students)
print(list(result))

# 对 age 从小到大排列
sort = sorted(students, key=lambda x: x.get('age'), reverse=True)
print(sort)