'''
Created on 2018年2月8日

@author: www60
'''
from _functools import reduce
from enum import Enum, unique
import logging
import pdb
logging.basicConfig(level=logging.INFO)


class Student(object):
    # 限制类中的属性 如果赋值其他属性 则报错
    __slots__ = ("__name", "__age")
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def to_string(self):
        return str(self.__class__) + "[" + "__age = " + str(self.__age) + ", __name = " + str(self.__name) + "]"
    
    """
@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，
只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器
@score.setter，负责把一个setter方法变成属性赋值，于是，
我们就拥有一个可控的属性操作：
    """

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, name):
        if(isinstance(name, str)):
            self.__name = name
        else:
            raise TypeError("类型错误！")

    """
    只定义getter方法，不定义setter方法就是一个只读属性：
    """

    @property
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if not isinstance(age, int):
            raise TypeError("类型错误")
        elif age > 100 or age < 0:
            raise ValueError("传入数值错误")
        else:
            self.__age = age


class GraduateStudent(Student):
    '''
    __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    '''
    pass


def func1():
    s = Student("小明", 22)
    s.set_name = "小明2号"
    s.set_age(99)
    print(s.to_string())
    if(hasattr(s, "score")):
        raise ValueError("内容出错")
    gs = GraduateStudent("小红", 20);
    gs.score = 35.35
    print(gs.to_string())


class RunnableMixIn(object):

    def run(self):
        print('Running...')


class FlyableMixIn(object):

    def fly(self):
        print('Flying...')


class CarnivorousMixIn(object):

    def eat(self):
        print("我是肉食动物")


class HerbivoresMixIn(object):

    def eat(self):
        print("我是植食动物")


class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物:
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    """
    Python 中一个子类可以继承多个父类
MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，
我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
    """
    pass


class Bat(Mammal, FlyableMixIn):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird, RunnableMixIn):
    pass


def func2():
    """
由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
只允许单一继承的语言（如Java）不能使用MixIn的设计。
Mixin思想在python中实现方式就是多重继承，但需要注意一些使用限制避免使类的关系复杂。
    Mixin类使用需要注意的限制：
        1）Mixin类功能需要单一，若要实现多个功能就需要创建多个Mixin类。
        2）其次Mixin类不依赖子类的实现，不能继承除了Mixin以外的类。
        3）不单独生成使用实例（理解为一个抽象类）。
    """
    d = Dog()
    # 查看当前类所继承的父类信息
    print(Dog.__mro__)
    print(d.__dir__())
    if(hasattr(d, "run")):
        d.run()
    if(hasattr(d, "eat")):
        d.eat()
    pass


class Students(object):

    def __init__(self, name):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b
        self.name = name

    # __str__()返回用户看到的字符串
    def __str__(self):
        return 'Student object (name=%s)' % self.name

    # __repr__()返回程序开发者看到的字符串
    # 通常__str__()和__repr__()代码都是一样的
    __repr__ = __str__

    def __iter__(self):
        """
        如果一个类想被用于for ... in循环，类似list或tuple那样，
        就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，
        Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
        直到遇到StopIteration错误时退出循环。
        """
        return self  # 实例本身就是迭代对象，故返回自己
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    def __getitem__(self, n):
        """
        Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
                实现__getitem__()方法 可以使用下标访问
        """
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        """
        __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice
        s所以要加上判断做相应的处理
        
                     也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
                    此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
                    与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
        """
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self):
        """
        __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数
                    ，把函数看成对象，因为这两者之间本来就没啥根本的区别。
        """
        print('My name is %s.' % self.name)

    __repr__ = __str__
#     __call__ = __getattr__


def func3():
#     for n in Students("a"):
#         print(n)
    s = Students("b")
    print(s[0:5])
    print(Chain().status.user.timeline.list)
    c = Chain("michael")
#     print(Chain().users("lisi").repos.a.b.c)
    c()
    """
          那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，
          我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，
          比如函数和我们上面定义的带有__call__()的类实例：
    """
    print(callable(c))
    print(callable(Students("b")))


@unique
class Month(Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12


def func4():
    """
    枚举遍历方法 __members__ 代表所有枚举属性 
    """
    for name, member in Month.__members__.items():
#         print(type(month)) #<class 'tuple'>
        print(name, '=>', member, ',', member.value)
#         for i in member:
#             print("{}\t\t{}".format(i, type(i)), end="\t")
#         print()
#         print("{}\t\t{}\t{}\t{}".format(member, member[0], member[1], member[1].value))
    # 当词典查看
#     print(Month.__members__)
    pass


class Hello(object):

    def hello(self, name='world'):
        print('Hello, %s.' % name)


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    """
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
metaclass，直译为元类，简单的解释就是：
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。
    """

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 关键字参数metaclass
class MyList(list, metaclass=ListMetaclass):
    """
当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时
，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，
比如，加上新的方法，然后，返回修改后的定义。__new__()方法接收到的参数依次是：
当前准备创建的类的对象；
    1.类的名字；
    2.类继承的父类集合；
    3.类的方法集合。
    """
    pass


def func5():
    h = Hello()
    h.hello()
    print(type(Hello))
    print(type(h))
    
    L = MyList()
    L.add(1)
    L.add(2)
    print(str(L))
    pass


def func6():
    """
    Python中异常的处理
    """
    print("------Begin------")
    try:
        print("try........")
        # 使用try...except捕获错误还有一个巨大的好处，就是可以跨越
        # 多层调用，比如函数main()调用foo()，foo()调用bar()，结果
        # bar()出错了，这时，只要main()捕获到了，就可以处理：
        bar('0')
        r = 10 / int("a")
        print("resule:%.2f" % r)
    except ValueError as e:
        print("except:{}".format(e))
    except ZeroDivisionError as e:
        print("except:{}".format(e))
    except BaseException as e:  # 所有的错误类型都继承自BaseException
        print("except:{}".format(e))
    finally:
        print("finally......")
    print("------End------")
    main()
#     foo1("0")
    s = '0'
    # 输入命令 n 可以单步执行代码
    # 输入命令 l 来查看代码
    # 输入命令 p 变量名来查看变量
    # 输入命令 q 结束调试，退出程序
    pdb.set_trace()
    n = int(s)
    """
          第三种调试方式  logging.info()
    """
# 需要显示日志信息需要在导包后添加日志级别 logging.basicConfig(level=logging.INFO)
    logging.info('n = %d' % n)
#     print(10 / n)
    '''
    第四种调试方式     python -m pdb err.py
    '''
    pass


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def str2num(s):
    try:
        return int(s)
    except:
        try:
            return float(s)
        except:
            raise ValueError("不是一个有效的数字");


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    assert r != 0, 'n is zero!'
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


def foo1(s):
    """
    调试第二种方式
    启动Python解释器时可以用-O参数来关闭assert
    """
    n = int(s)
    # assert的意思是，表达式n != 0应该是True，
    # 否则，根据程序运行的逻辑，后面的代码肯定会出错。
    # 如果断言失败，assert语句本身就会抛出AssertionError：
    assert n != 0, 'n is zero!'
    return 10 / n


def test():
    func6()
    pass


if __name__ == '__main__':


#     func1();
#     func2()
#     func3()
#     func4()
#     func5()
    test()


    pass

