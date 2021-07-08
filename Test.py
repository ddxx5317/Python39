import keyword
import sys
import math
import pickle
import glob
from datetime import date
import re
import calendar
import time

print(keyword.kwlist)


# 可写函数说明
def printinfo(name, age=35):
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')

# 打开一个文件
f = open("foo.txt", "w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
f.close()

f = open("foo.txt", "r")
str = f.read()
print(str)
f.close()


f = open("foo.txt", "r")
for line in f:
    print(line, end='')
f.close()

print("-------------------")


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

print(glob.glob('*.py'))


now = date.today()
print(now)


print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

ticks = time.time()
print("当前时间戳为:", ticks)
localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

cal = calendar.month(2021, 7)
print("以下输出2016年1月份的日历:")
print(cal)