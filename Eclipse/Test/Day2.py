# -*- coding: utf-8 -*-
'''
Created on 2018年2月6日

@author: www60
'''
from collections import Iterable
import locale
import math
import os
import random
import sys
import time

locale.setlocale(locale.LC_CTYPE, "chinese")


def func(odd, even, num):
    if(num % 2 == 0):
        even.append(num)
    else:
        odd.append(num)


def func2():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    even = []
    odd = []
    while len(numbers) > 0:
        number = numbers.pop()
        if number % 5 == 0:
            break
        if number % 3 == 0 :
            continue
        if(number % 2 == 0):
            even.append(number)
        else:
            odd.append(number)
    print("even:{a}".format(a=even))
    print("odd:" + str(odd))
    
    while len(odd) > 0:
#         num = int(input("请输入:"))
        num = int(random.uniform(1, 100))
        func(odd, even, num)
        print("输入的是：{}\nodd:{s1}\neven:{s2}".format(num, s1=odd, s2=even), end="\n")
        time.sleep(1)
        if(10 not in odd or 10 not in even):
            print("还没有出现10,时间：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))))
        if len(odd) > 10 or len(even) > 10:
            break


def func3():
    print(sys.getdefaultencoding())
    date = input("输入时间（格式如：2017-04-04）:")
    t = time.strptime(date, "%Y-%m-%d")
    print(time.strftime(('今年的第%j天'), t))


def func4():
    '''
    list和tuple是Python内置的有序集合，一个可变，一个不可变。
    '''
    classmates = ["a", "b", "c"]
    # 获取list元素的个数
    lens = len(classmates)
    print("list的长度为{len}".format(len=lens))
    for i in classmates:
        print(i)
    # 删除list指定元素 若无数字则默认删除末尾元素
    classmates.pop(2)
    # list中追加元素到末尾
    classmates.append("d")
    # 元素插入到指定的位置，比如索引号为1的位置：
    classmates.insert(2, "e")
    # 数组
    t = (1,)  # 新建一个只有一个元素的元组
    print(t)
    t1 = ('a', 'b', ['A', 'B'])
    print(t1[2][0] + "\t" + t1[2][1])
    print(t1)
    L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['Adam', 'Bart', 'Lisa']
    ]
    print(L[0][0])  # 打印Apple
    print(L[1][1])  # 打印Python
    print(L[2][2])  # 打印Lisa
    L.sort()  # 排序操作
    print(L)


def func5():
    sum = 0  # @ReservedAssignment
    for i in range(101):
        sum += i
    print(sum)


def func6():
    """
    dict和list比较，dict有以下几个特点：
            查找和插入的速度极快，不会随着key的增加而变慢；
            需要占用大量的内存，内存浪费多。
    list相反：
            查找和插入的时间随着元素的增加而增加；
            占用空间小，浪费内存很少。
    """
    # 相当于HashMap
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print(d["Michael"])
    # 用get 如果没有值不会报错，也可指定未找到返回结果
    print(d.get("Bobs", -1))
    # 删除一个key，对应的value也会从dict中删除
    d.pop("Tracy")
    # 可以用in 来判断元素是否在dict中 查找
    print("abc" in d)


def func7():
    '''
    set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
    '''
    s = set([1, 2, 3])
    s2 = set([2, 3, 4])
    print(s)
    # 添加set中元素
    s.add(4)
    # 删除set中元素
    s.remove(4)
    # 修改set中元素
    s.update("666")
    # 查找set中元素
    for i in s2:
        print(i)
    print(s | s2)
    print("1" in s2)


def func8():
    # 求绝对值
    print(abs(-10))
    # 求最大值
    print(max(5, 7, 9, 2, 9, 7, 5, 5, 8, 7, 5))
    # 强制类型转换
    i = int("12")
    # 把一个整数转换成十六进制表示的字符串
    print(hex(i + 5))

    
def nop():
    '''
    定义一个空函数
    '''
    pass


def my_abs(x):
    # 对参数类型做检查    数据类型检查函数 isinstance
    if not isinstance(x, (int, float)):
        raise TypeError("这是一个错误的传参类型");
    if x >= 0:
        return x
    else:
        return -x

    
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 默认参数必须指向不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


def num_adds(*num, sum=0):  # @ReservedAssignment
    for i in num:
        sum += i
    return sum


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def func9():
    """
    Python函数返回的仍然是单一值返回值是一个tuple
    """
    x, y = move(100, 100, 60, math.pi / 6)
    print("x轴：{}\ny轴：{}".format(x, y))
    print(add_end([1, 23, 4, 5, 6, 8]))
    print(num_adds(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(fact(10))


def func10():  # 摇筛子游戏
    result = []
    while True:
        result.append(int(random.uniform(1, 7)))
        result.append(int(random.uniform(1, 7)))
        result.append(int(random.uniform(1, 7)))
        print(result)
        count = 0
        index = 2
        pointStr = ""
        while index >= 0:
            currPoint = result[index]
            count += currPoint
            index -= 1
            pointStr += " "
            pointStr += str(currPoint)
        if count <= 11:
            sys.stdout.write(pointStr + " -> " + "小" + "\n")
            time.sleep(1)  # 睡眠一秒
        else:
            sys.stdout.write(pointStr + " -> " + "大" + "\n")
            time.sleep(1)  # 睡眠一秒
        result = []


def func11():
    """
    切片操作
    """
    list1Display = ['1', '2', '3', '4', '5', '6', '7', '8']
    list2Display = ['abc', 'def', 'rfs']
    # 切片 两种形式 若从0开始可省略
    print(list1Display[0:2])
    sys.stdout.write(str(list2Display[:2]))
    # 倒着取数
    print(list1Display[-1:])
    # 前5个数，每两个取一个：
    print(list1Display[:5:2])
    # 所有数，每3个取一个：
    print(list1Display[::3])
    '''
    tuple也是一种list，唯一区别是tuple不可变
    '''
    print((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)[::3])


def func12():
    '''
    迭代:str可以迭代：list可以迭代
    '''
    arr = "abcdefghikmlnopqrstuvwxyz"
    print(isinstance(arr, Iterable))
    # enumerate函数可以把一个list变成索引-元素对
    for i, value in enumerate(arr):
        if(i % 10 == 0):
            print()
        print(i, value, end="\t")
    sys.stdout.write("\n")
    for x, y in [(1, 1), (2, 4), (3, 9)]:
        print(x, y)
    result = [m + n for m in 'ABC' for n in 'XYZ']
    print(result)
    result1 = [d for d in os.listdir('.')]
    print(result1)
    result2 = [x * x for x in range(1, 11) if x % 2 == 0]
    print(result2)
    """
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
    """
    # 首先获得Iterator对象:
    it = iter(result2)
    # 循环:
    while True:
        try:
            # 获得下一个值:
            x = next(it)
        except StopIteration:
            # 遇到StopIteration就退出循环
            break


def main():
    '''
    str是不变对象，而list是可变对象。
    '''

#     func2();
#     func3();
#     func4();
#     func5();
#     func6();
#     func7();
#     func8();
#     print(my_abs(-5));
#     func9();
#     func10();
# 输出调用系统的控制窗口
#     os.system("adb shell input swipe 100 100 900 900 2000")
#     func11();
    func12();
#     func12();

    
if __name__ == '__main__':


    main()
    
