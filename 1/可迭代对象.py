from filecmp import cmp

__author__ = 'Darr_en1'



# 在python中对list进行排序有两种方法：
#
# 1.用List的成员函数sort进行排序(list适用)  本对象操作
# 2.用built-in函数sorted进行排序(可迭代对象通用)  生成新的对象(list)



# 对str进行去重排序


str="cdsciolsdruikcadssv"
s = list(set(str))
s.sort(reverse=False)
print("".join(s))

print("".join(sorted(set(str),reverse=False)))



old_dict={"name":"zs","age":23,"city":"shanghai"}
print(old_dict)
new_dict = dict(sorted(old_dict.items(),key=lambda i:i[0],reverse=False))
print(new_dict)


# 字符串也是可迭代对象
print(sorted("hello world"))



#  zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
#  然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
#
# 我们可以使用 list() 转换来输出列表。
#
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，
# 利用 * 号操作符，可以将元组解压为列表。
a = [1,2]
b = [3,4,5]

list_obj = list(zip(a,b))
dict_obj = dict(zip(a,b))

c,d = zip(a,b)

h,f = zip(*zip(a,b))

print(list_obj)
print(dict_obj)
print(c,d)
print(h,f)
