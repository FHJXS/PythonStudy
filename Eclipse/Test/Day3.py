# -*- coding: UTF-8 -*-
'''
Created on 2018��2��7��

@author: www60
'''

from builtins import map
from cgi import log
from datetime import date
from functools import reduce
from types import MethodType

from numpy import sort

__author__ = "LiJie"


def func1(a, b, f):
    '''
    高阶函数
    '''
    return f(a) + f(b)


def func2(x):
    return x * x


def func_3():
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def fn(x, y):
        return x * 10 + y
    
    def char2num(s):
        return digits[s]

    return reduce(fn, list(map(char2num, "13579")))


def func3():
    # map函数使用 传入函数，及处理数据
    print(list(map(func2, sort([x for x in range(1, 11)]))))
    print(list(map(str, [x for x in range(1, 11)][::2])))
    
    # reduce 把一个函数作用在一个序列上这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
    # 例：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    print(func_3());


def func4():
    '''
    filter 使用
    '''

    def is_odd(n):
        return n % 3 == 1
    
    print(list(filter(is_odd, range(1, 51))))

    # 构造一个从3开始的奇数序列
    def _odd_iter():
        n = 1
        while True:
            n = n + 2
            yield n

    # 定义一个筛选函数
    def _not_divisible(n):
        return lambda x: x % n > 0

    # 定义一个生成器，不断返回下一个素数
    def primes():
        yield 2
        it = _odd_iter()  # 初始序列
        while True:
            n = next(it)  # 返回序列的第一个数
            yield n
            it = filter(_not_divisible(n), it)  # 构造新序列

    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

    # python 自带sorted函数
    print(sorted([36, 5, -12, 9, -21], key=abs))
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
    # 反向排序
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
    # 选中key进行排序
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    print(sorted(L, key=lambda x:x[1]))


def func5():
    '''
    高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
    '''

    def lazy_sum(*args):

        def sum():  # @ReservedAssignment
            ax = 0
            for n in args:
                ax = ax + n
            return ax

        return sum

    f = lazy_sum(1, 3, 5, 7, 9)
    print(f())
    
    # 匿名函数 lambda
    L = list(filter(lambda x:x % 2 == 1, range(1, 20)))
    print(L)


def func6():
    '''
在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。
decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
    '''

    def deftion(x):
        return x * x

    num = list(map(deftion, range(1, 10)))
    print(num)
    # 当前类 类别
    print(num.__class__)
    # 当前类  说明
    print(num.__doc__)
    # 当前类 数组长度
    print(num.__len__())
    
    def log(text):

        def decorator(func):

            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)

            return wrapper

        return decorator
    
    @log("execute")
    def now():
        print(date.today())
    
    now()
    
    # 可以用来做N进制的转换   偏函数
    num = int("100", base=8)
    print(num)
    num1 = int("100", 8)
    print(num1)


class Student(object):

    def __init__(self, name, score):
        self.__name = name  # 私有变量
        self.__score = score  # 公有变量
    
    def print_stuinfo(self):
        print("%s\t:%s\t" % (self.__name, self.__score))
    
    # 同样需要get set 方法
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


def func7():
    stu = Student("abc", 123)
    stu2 = Student("def", 456)
    Student.print_stuinfo(stu)
    Student.print_stuinfo(stu2)


class Animal(object):

    def run(self):
        print("在{}中运行run方法".format(self.__class__))


class Dog(Animal):

    # 覆盖父类的方法
    def run(self):
        print('Dog正在运行')
    
    def eat(self):
        print("Dog正在吃")


class Cat(Animal):
    pass


class Pik(object):

    def run(self):
        print("Pik在运行中")


def func8():
    c = Cat()
    d = Dog()
    a = Animal()
    p = Pik()
    c.run()
    d.run()
    # Python这样的动态语言来说，则不一定需要传入Animal类型
    # 我们只需要保证传入的对象有一个run()方法就可以了
    Animal.run(p)
    # 判断是否为 此类的对象
    print(isinstance(a, Cat))
    print(isinstance(c, Animal))  # 此对象的父类为 Animal
    print(isinstance(c, Cat))
    print(isinstance(d, Dog))

    
def func9():
    # 用来判断基本类型
    print(type(123))
    print(type(1.56))
    print(type("abc"))
    print(type((1,)))
    print(type([1, 2]))
    print(type({'2':2}))
    print(type(None))
    # 如果要获得一个对象的所有属性和方法，可以使用dir()函数，
    # 它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
    print(dir("abc"))
    # lower()返回小写的字符串
    print("ABC".lower())
    # lower()返回大写的字符串
    print("abc".upper())

    class MyObject(object):
        obj = "ccc"

        def __init__(self):
            self.x = 9

        def power(self):
            return self.x * self.x
    
    objs = MyObject()
    print(hasattr(objs, 'x'))  # 有属性'x'或者方法吗？
    setattr(objs, 'y', 19)  # 设置一个属性'y'
    # 如果试图获取不存在的属性，会抛出AttributeError的错误：
    print(getattr(objs, 'y'))  # 获取属性'y'
    # 千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
    print(MyObject.obj)  # ccc
    print(objs.obj)  # ccc
    objs.obj = "bbb"  
    print(MyObject.obj)  # ccc
    print(objs.obj)  # bbb


class Stu(object):
    pass


def test():

    def set_age(self, age):
        self.age = age
        
    s = Stu()
    # 给类绑定方法
    s.set_age = MethodType(set_age, s)
    s.set_age(5)
    print(s.age)
    return "hello,%s" % __author__


if __name__ == '__main__':


#     func_1 = func1(-3, -5, abs)
#     print(func_1)
#     func3()
#     func4()
#     func5()
#     func6()
#     func7()
#     func8()
#     func9()
    print(test())
