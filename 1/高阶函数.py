from functools import reduce

__author__ = 'Darr_en1'

# 高阶函数

#  在python中，函数本身也可以赋值给变量，即：变量可以指向函数。
#  编写高阶函数，就是让函数的参数能够接收别的函数。

# map
# map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次
# 作用到序列的每个元素，并把结果作为新的list返回。

# reduce
# reduce()必须接收两个参数，reduce把上一个计算的结果继续和序列的下一个元素做累积计算

# filter
# Python内建的filter()函数用于过滤序列。filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。


# sorted
#  sorted()函数接收函数，序列，进行排序

# 列表推导式+高阶函数map
res  =[ re for re in map(lambda x: x*x, [1,2,3,4,5]) if re >10]

print(list(res))

# 高阶函数filter + map
res  =list(filter(lambda x:x>10,map(lambda x: x*x, [1,2,3,4,5])))

print(res)


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

#  高阶函数reduce + map 将字符串转化成整数
def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))


print(str2int("3456"))
