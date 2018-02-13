# -*- coding: UTF-8 -*-
'''
Created on 2018年2月9日

@author: www60
'''
from _io import StringIO, BytesIO
import doctest
import json
from multiprocessing import Process
import os
from plistlib import Dict
import re
from sys import path
import unittest


class TestDict(unittest.TestCase):

    def test_init(self):
        print("测试初始化")
        try:
            d = Dict(a=1, b="test")
            self.assertEqual(d.a, 1)
            self.assertEqual(d.b, "test")
            self.assertTrue(isinstance(d, dict))
        except Exception as e:
            print("Error : {}".format(e))
    
    def test_key(self):
        print("测试key赋值获取")
        try:
            d = Dict()
            d["key"] = "value"
            self.assertEqual(d.key, "value")
        except Exception as e:
            print("Error : {}".format(e))
        
    def test_attr(self):
        try:
            d = Dict()
            d.key = "value"
            self.assertTrue("key" in d)
            self.assertEqual(d['key'], "value")
        except Exception as e:
            print("Error : {}".format(e))

    def test_keyerror(self):
        print("测试key错误赋值")
        try:
            d = Dict()
            with self.assertRaises(KeyError):
                value = d["empty"]  # @UnusedVariable
        except Exception as e:
            print("Error : {}".format(e))

    def test_attrerror(self):
        print("测试属性错误赋值")
        try:
            d = Dict()
            with self.assertRaises(AttributeError):
                value = d.empty  # @UnusedVariable
        except Exception as e:
            print("Error : {}".format(e))

    # 类似于 java单元测试中的 @before
    def setUp(self):
        print("开始")
        
    # 类似于 java 中 @after 
    def tearDown(self):
        print("结束")


def func1():
    """
    单元测试
    """
    # 第一种单元测试 直接运行unittest.main() 可普通运行
    unittest.main()
    # 第二种单元测试  python -m unittest mydict_test
    pass


class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def func2():
    m = re.search("(?<=abc)(def)", "abcdef")
    print(m.group(0))
    # 只有在命令行直接运行时，才执行doctest。
    # 所以，不必担心doctest会在非测试环境下执行。
    doctest.testmod()
    pass


def func3():
    """
    在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。
    """
#     try:
#         file = open("%s/resource/test.txt" % path[0], 'r')
# #         print(file.__dir__())
#         print(file.read())
#     finally:
#         if file:
#             file.close()
    # 普通方式打开
    with open("%s/resource/test.txt" % path[0], 'r') as f:
        for len in f.readlines():  # @ReservedAssignment
            print(len , end="")
    # 二进制编码打开
    with open("%s/resource/test.txt" % path[0], 'rb') as f:
        for len in f.readlines():  # @ReservedAssignment
#             print(len.strip()) # 把末尾的'\n'删掉
            print(len , end="")
    # 字符编码打开
#     with open("%s/resource/test.txt" % path[0], 'r', encoding='gbk') as f:
#         for len in f.readlines():  # @ReservedAssignment
#             print(len , end="")
    # 写文件 w:普通写 wb:二进制写入  a :追加写入
    with open("%s/resource/test.txt" % path[0], 'w') as f:
        f.write("今天股市跌停了，损失惨重！\n")
        f.write("大盘崩了！\n")
    pass


def func4():
    """
    StringIO顾名思义就是在内存中读写str。
    """
    f = StringIO("可以这样初始化#\t#\t")
#     f = StringIO()
    f.write("HelloWorld!")  # 后面写入会覆盖初始化
    print(f.getvalue())  # getvalue()方法用于获得写入后的str。
    """
    StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
    """
    fb = BytesIO()
#      f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')#也可以这样初始化
    fb.write("测试中文".encode(encoding='utf_8'))
    print(fb.getvalue())
    pass


def func5():
    """
    把两个路径合成一个时，不要直接拼字符串，
    而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
    同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
    这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
    """
    # 在操作系统中定义的环境变量，全部保存在os.environ这个变量中
    print(os.environ.get("path", "-1"))  # 若未找到则默认返回-1
    # 查看当前目录的绝对路径:
    print(os.path.abspath("."))
    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
    print(os.path.join("C:\\Users\\www60\\workspace\\Test\\resource", 'testdir'))
    # 然后创建一个目录:
    os.mkdir("C:\\Users\\www60\\workspace\\Test\\resource\\testdir")
#     print("创建成功，5秒后自动删除！")
#     sleep(5)
#     # 删掉一个目录:
#     os.rmdir("C:\\Users\\www60\\workspace\\Test\\resource\\testdir")
#     print("删除成功！")
    # 分切文件名和目录 用os.path.split 可以拆分两块
    print(os.path.split("C:\\Users\\www60\\workspace\\Test\\resource\\test.txt"))
    # os.path.splitext()可以直接让你得到文件扩展名
    print(os.path.splitext("C:\\Users\\www60\\workspace\\Test\\resource\\test.txt"))
    # 对文件重命名
    os.renames("resource/test.txt", "resource/test.py")
    # 删除目录 及以下的文件
    os.removedirs("resource\\testdir")
    os.renames("resource/test.py", "resource/test.txt")
    # 列出所有以.py的文件  
    print([x for x in os.listdir(".") if not os.path.isdir(x) and os.path.splitext(x)[1] == ".py"])
    print("============开始遍历===========")
    dg(path[0], endType=".py")
    print("============结束遍历===========")
    pass


def dg(path, endType="", fandAll=True):
#     if(path.__dir__())
    for x in os.listdir(path):
        repath = os.path.join(path , x)
        if(fandAll and not x.startswith('.')):
            if(os.path.isdir(repath)):
#                 print("文件夹：[{}]".format(repath))
                dg(repath, endType, fandAll)
            else:
                if(os.path.isfile(repath) and x.endswith(endType)):
                    print("\t" + repath)
        else:
            if(os.path.isfile(repath) and x.endswith(endType)):
                print("\t" + repath)
            else:
#                 print("文件夹：[{}]".format(repath))
                pass
    pass


def func6():
    import pickle
    d = dict(name="Bob", age=20, score=88)
    # Python提供了pickle模块来实现序列化
    print(pickle.dumps(d))
    """
    pickle.dumps()方法把任意对象序列化成一个bytes，然后，
        就可以把这个bytes写入文件。或者用另一个方法pickle.dump()
        直接把对象序列化后写入一个file-like Object：
    """
    f = open("resource/test.txt", 'wb')
    # pickle.dump()直接把对象序列化后写入一个file
    pickle.dump(d, f)
    f.close()
    f = open("resource/test.txt", 'rb')
    # 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
    # 然后用pickle.loads()方法反序列化出对象
    # 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
    d = pickle.load(f)
    f.close()
    print(d)
    print("JSON字符串：\n\t" + json.dumps(d))

    class Student(object):

        def __init__(self, name, age, score):
            self.name = name
            self.age = age
            self.score = score

        def student2dict(self):  # @DontTrace
            return {
                'name': self.name,
                'age': self.age,
                'score': self.score
            }
    
    s = Student('Bob', 20, 88)
    print(json.dumps(s.__dict__))
    # 需要设置默认的方法 首先转换成dict对象
    print("class对象转JSON字符串：\n\t" + json.dumps(s, default=Student.student2dict))
    # 默认使用 __dict__ 的方法把对象转换为 dict
    print("class对象转JSON字符串：\n\t" + json.dumps(s, default=lambda obj: obj.__dict__))
    # json 反序列化成一个对象 loads
    j = json.loads(json.dumps(s.__dict__, ensure_ascii=True))
    print(type(j))
    pass

#     arr = "abcdefghikmlnopqrstuvwxyz"
#     for value in enumerate(arr):
#         print(type(value))  #<class 'tuple'>
#         print(value)   #(0, 'a')


def func7():
    print("%s ---- %s" % (os.getpid(), os.getppid()))
    print(os.getlogin())


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def test():
    func7();
    pass


if __name__ == '__main__':
    """
创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，
用start()方法启动，这样创建进程比fork()还要简单。
join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    """
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))  # 创建进程P
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
    pass
#     func1()
#     func2()
#     func3()
#     func4()
#     func5()
#     func6();
#     test()
#     pass
