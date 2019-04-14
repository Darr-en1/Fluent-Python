import re

__author__ = 'Darr_en1'


# 通过re匹配str中的中文

a = "not 404 found 张三 99 北京"

re_1 = re.findall('[^\x00-\xff]+',a)
re_2 = re.findall('[\u4e00-\u9fa5]+',a)
print(re_1,re_2)



# 贪婪匹配(.*)          满足正则的尽可能多的匹配
# 非贪婪匹配(.*?)       满足正则的尽可能少的匹配

s = "<a>呵呵</a><a>哈哈</a>"
re_3 =re.findall("<a>(.*)</a>",s)
re_4 =re.findall("<a>(.*?)</a>",s)

print(re_3,re_4)


# re 修改字符串
a = "zt 考试得了98分"

ret = re.sub(r"\d+","100",a)
print(ret)
