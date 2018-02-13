# -*- coding: UTF-8 -*-
import hmac
import json
import random
import struct
import urllib
from contextlib import contextmanager, closing
from datetime import datetime, timedelta
import time
import locale

import sys
from urllib import request, parse
from urllib.request import urlopen

from numpy.core.tests.test_mem_overlap import xrange

locale.setlocale(locale.LC_CTYPE, 'chinese')


def func01():
    # 获取当前日期和时间
    now = datetime.now()
    print(now)
    print(type(now))
    # 获取指定日期和时间
    dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
    print(dt)
    # datetime类型转换为timestamp只需要简单调用timestamp()方法
    temp = dt.timestamp()
    print(temp)
    # 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法
    print(datetime.fromtimestamp(temp))
    # 查看 UTC 时间
    print(datetime.utcfromtimestamp(temp))
    # str 转化为 datetime
    cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
    print(cday)
    # str转date型
    t = time.strptime('2018-2-15 00:00:00', '%Y-%m-%d %H:%M:%S')
    # print(seconds)
    # date型转str
    seconds = int(int(time.mktime(t)) - time.time())
    # sys.stdout.write("%s \r" % time.strftime(('距离%Y年%m月%d日 %H小时%M分钟%S秒 还剩'+seconds+"秒"), t), )
    # sys.stdout.flush()
    # interface_show(title=time.strftime(('距离%Y年%m月%d日 %H小时%M分钟%S秒 还剩'), t), artist=" ", rate=" ", minutes=seconds)
    # datetime 加减
    now = datetime.now()
    print(now + timedelta(hours=10))
    print(now - timedelta(days=1))
    print(now + timedelta(days=2, hours=12))
    pass


def interface_show(**kwargs):
    lineTmpla = ' ' * 5 + kwargs['title'] + kwargs['artist'] + kwargs['rate'] + " %-3s"
    print
    (time_remain(lineTmpla, kwargs['minutes']),)


def time_remain(lineTmpla, mins):
    count = 0
    while (count < mins):
        count += 1
        n = mins - count
        time.sleep(1)
        sys.stdout.write("\r" + lineTmpla % (n) + "  秒", )
        sys.stdout.flush()
        if not n:
            return 'completed'


from collections import namedtuple, deque, OrderedDict, Counter


def func02():
    """
    namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
    并可以用属性而不是索引来引用tuple的某个元素。
    :return:
    """
    # 相当于创建一个类
    Point = namedtuple("Point", ['x', 'y'])
    p = Point(1, 2)
    print("x = %d, y = %d" % (p.x, p.y))
    print(isinstance(p, Point))
    # namedtuple('名称', [属性list]):
    Circle = namedtuple('Circle', ['x', 'y', 'r'])
    c = Circle(1, 2, 3)
    print(c)  # 也是一种集合
    """
    使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
    因为list是线性存储，数据量大的时候，插入和删除效率很低。
    deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
    """
    q = deque(['a', 'b', 'c'])
    q.append("x")
    q.appendleft("y")
    """
    deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
    这样就可以非常高效地往头部添加或删除元素。
    """
    q.pop()
    q.popleft()
    print(q)
    """
    使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
    如果要保持Key的顺序，可以用OrderedDict：
    """
    d = dict([('a', 1), ('b', 2), ('c', 3)])
    print(d)  # dict的Key是无序的
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(od)  # OrderedDict的Key是有序的
    """
    Counter是一个简单的计数器，例如，统计字符出现的个数：
    """
    c = Counter()
    for ch in 'programming':
        c[ch] = c[ch] + 1
    print(c)


class LastUpdatedOrderedDict(OrderedDict):
    """
    OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
    """

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


import base64


def func03():
    # 编码
    print(base64.b64encode('李杰'.encode()))
    # print(b'5p2O5p2w'.decode(encoding='UTF-8'))
    # 解码
    print(base64.b64decode(b'5p2O5p2w'))
    print(b'\xe6\x9d\x8e\xe6\x9d\xb0'.decode(encoding='UTF-8'))
    """
    由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数
    ，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成
    -和_：
    """
    print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    print(base64.urlsafe_b64decode('abcd--__'))
    pass


def func04():
    # 一个32位无符号整数变成字节
    n = 10240099
    b1 = (n & 0xff000000) >> 24
    b2 = (n & 0xff0000) >> 16
    b3 = (n & 0xff00) >> 8
    b4 = n & 0xff
    bs = bytes([b1, b2, b3, b4])
    print(bs)
    """
    Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
    struct的pack函数把任意数据类型变成bytes：
    pack的第一个参数是处理指令，'>I'的意思是：
        I：4字节无符号整数和
        H：2字节无符号整数。
    >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
    后面的参数个数要和处理指令一致。
    """
    print(struct.pack('>I', 10240099))
    print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
    bmp_data = base64.b64decode(
        'Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
    print(bmp_data)
    pass


import hashlib


def func05():
    """
    MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
    如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
    :return:
    """
    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())

    md5_d = hashlib.md5()
    md5_d.update('how to use md5 in '.encode('utf-8'))
    md5_d.update('python hashlib?'.encode('utf-8'))
    print(md5_d.hexdigest())

    """
    SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
    比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，
    而且摘要长度更长。
    """
    sha1 = hashlib.sha1()
    sha1.update('how to use sha1 in '.encode('utf-8'))
    sha1.update('python hashlib?'.encode('utf-8'))
    print(sha1.hexdigest())

    pass


def func06():
    """
    如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message + salt)。但实际上，把salt看做一个“口令”，加salt的哈希就是：
    计算一段message的哈希时，根据不通口令计算出不同的哈希。要验证哈希值，必须同时提供正确的口令。
    这实际上就是Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
    和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是
    MD5还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。
    Python自带的hmac模块实现了标准的Hmac算法。
    :return:
    """
    message = b'Hello, world!'
    key = b'secret'
    # 如果消息很长，可以多次调用h.update(msg)
    h = hmac.new(key, message, digestmod='MD5')
    print(h.hexdigest())
    pass


import itertools


def func07():
    """
    itertools提供的几个“无限”迭代器：
    :return:
    """
    i = 0;
    natuals = itertools.count(1)
    for n in natuals:
        print(n, end=" ")
        i = i + 1
        if i > 10:
            break

    print()
    i = 0;
    # cycle()会把传入的一个序列无限重复下去：
    cs = itertools.cycle("ABC")  # 注意字符串也是序列的一种
    for c in cs:
        print(c, end=" ")
        i = i + 1
        if i > 10:
            break
    print()
    """
    repeat()负责把一个元素无限重复下去，不过如果提供第二个参数
    就可以限定重复次数：
    """
    ns = itertools.repeat('A', 3)
    for n in ns:
        print(n, end=" ")
    print()
    """
    无限序列虽然可以无限迭代下去，但是通常我们会通过
    takewhile()等函数根据条件判断来截取出一个有限的序列：
    """
    natuals = itertools.count(1)
    ns = itertools.takewhile(lambda x: x <= 10, natuals)
    print(list(ns))
    """
    chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
    """
    for c in itertools.chain('ABC', 'XYZ'):
        print(c, end=" ")
    pass
    """
    groupby()把迭代器中相邻的重复元素挑出来放在一起：
    """
    for key, group in itertools.groupby('AAABBBCCAAA'):
        print(key, list(group))
    """
    实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的
    值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key
    。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
    """
    for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
        print(key, list(group))


def func08():
    """
    并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象
    ，只要正确实现了上下文管理，就可以用于 with 语句。
    实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如
    ，下面的class实现了这两个方法：
    :return:
    """

    # class Query(object):
    #
    #     def __init__(self, name):
    #         self.name = name
    #
    #     def __enter__(self):
    #         print('Begin')
    #         return self
    #
    #     def __exit__(self, exc_type, exc_value, traceback):
    #         if exc_type:
    #             print('Error')
    #         else:
    #             print('End')
    #
    #     def query(self):
    #         print('Query info about %s...' % self.name)

    # with Query('Bob') as q:
    #     q.query()
    """
    编写__enter__和__exit__仍然很繁琐，因此Python的标准库
    contextlib提供了更简单的写法，上面的代码可以改写如下
    """

    class Query(object):
        def __init__(self, name):
            self.name = name

        def query(self):
            print('Query info about %s...' % self.name)

    """
    代码的执行顺序是：
        1.with语句首先执行yield之前的语句，因此打印出 Begin ；
        2.yield调用会执行with语句内部的所有语句，因此打印出hello和world；
        3.最后执行yield之后的语句，打印出 End 。
    因此，@contextmanager让我们通过编写generator来简化上下文管理。
    """

    @contextmanager
    def create_query(name):
        print('Begin')
        q = Query(name)
        yield q
        print('End')

    with create_query('Bob') as q:
        q.query()

    """
    如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，
    可以用closing()来把该对象变为上下文对象。例如，用with语句使用
    urlopen()：
    """
    with closing(urlopen('http://www.baidu.com')) as page:
        for line in page:
            print(line)

    # @contextmanager
    # def closing(thing):
    #     try:
    #         yield thing
    #     finally:
    #         thing.close()
    # 它的作用就是把任意对象变为上下文对象，并支持with语句。
    pass


def func09():
    with request.urlopen("https://www.douban.com/about") as f:
        data = f.read()
        print("Status", f.status, f.reason)
        for k, v in f.getheaders():
            print('%s : %s' % (k, v))
        print('Data:', data.decode('utf-8'))
    pass


def func10():
    """
    如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，
    通过往Request对象添加HTTP头，
    我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：
    :return:
    """
    req = request.Request("http://www.douban.com/")
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print("Status:",f.status,f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))
    pass


def func11():
    print('Login to weibo.cn...')
    # email = "www.609446687@qq.com"#input('Email: ')
    # passwd ="17671302700lijie" #input('Password: ')
    login_data = parse.urlencode([
        ('mod_type' ,'mod/pagelist'),
        ('maxPage' ,'50'),
        ('page', '1'),
        ('url', '/feed/friends?version=v4'),
        ('previous_cursor', '4206281708954922'),
        ('next_cursor' , '4206268128943854'),
        # ('loadMore','False'),
        # ('M_WEIBOCN_PARAMS', 'uicode%3D20000174'),
        # ('SCF', 'AgorSYqMGG8q6dGPaKqQylYOpRKiFxoSlM8_n2BxPB9X35UTinYUIgrN1aFFB5pz4BX9hlDlInWsJ5duEYygI74.'),
        # ('SUB', '_2A253hHJkDeRhGeRK6lsT8yrFzD'),
        # ('WEIBOCN_FROM', 'f6836b0cdcbe863a3ce243169cc55999')
    ])

    req = request.Request('https://m.weibo.cn/feed/friends?version=v4')
    req.add_header('Cookie', '_T_WM=f6836b0cdcbe863a3ce243169cc55999; OUTFOX_SEARCH_USER_ID_NCOO=1137577305.201728; SUB=_2A253hHJkDeRhGeRK6lsT8yrFzD-IHXVUhx4srDV6PUJbkdANLUnNkW1NU3WoHBidLmY4eYTlRKSzNyPqEalmza3H; SUHB=0S7DZNBE109Kxl; SCF=AgorSYqMGG8q6dGPaKqQylYOpRKiFxoSlM8_n2BxPB9X35UTinYUIgrN1aFFB5pz4BX9hlDlInWsJ5duEYygI74.; SSOLoginState=1518338612; M_WEIBOCN_PARAMS=uicode%3D20000174')
    req.add_header('User-Agent','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1')
    # req.add_header('Referer','https://m.weibo.cn/?&jumpfrom=weibocom')
    with request.urlopen(req,data=login_data.encode('gb2312')) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        # data = f.read()
        print('Data:', f.read().decode('gb2312'))


    pass


def func12():
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
    opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
    with opener.open('http://www.example.com/login.html') as f:
        f.getheaders
        pass
    pass


def test():
    # func01()
    # func02()
    # func03()
    # func04()
    # func05()
    # func06()
    # func07()
    # func08()
    # func09()
    # func10()#get request
    func11()#Post
    # func12()
    pass


if __name__ == '__main__':
    test()
    # def pi(N):
    #     ' 计算pi的值 '
    #     # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    #     natuals = itertools.count(1)
    #     ns = itertools.takewhile(lambda x: x < N, natuals)
    #     # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    #     counts = list(ns)[::2]
    #     # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    #     j = 0;
    #     sum = 0.0;
    #     begin = time.time()
    #     for i in counts:
    #         if (j % 2 == 0):
    #             sum = sum + 4.0 / i
    #         else:
    #             sum = sum + -4.0 / i
    #         j = j + 1
    #     # step 4: 求和:
    #     end = time.time()
    #     # print("总共计算：%f 次，耗时 %s 秒"%(j,str(end-begin)))
    #     print("本计算机的处理速度为: %d 次/秒"%int(j/(end-begin)))
    #     return sum
    #
    #
    # print(pi(99999))
    # scale = 10000
    # maxarr = 2800
    # arrinit = 2000
    # carry = 0
    # arr = [arrinit] * (maxarr + 1)
    # for i in xrange(maxarr, 1, -14):
    #     total = 0
    #     for j in xrange(i, 0, -1):
    #         total = (total * j) + (scale * arr[j])
    #         arr[j] = total % ((j * 2) - 1)
    #         total = total / ((j * 2) - 1)
    #     sys.stdout.write("%04d" % (carry + (total / scale)))
    #     carry = total % scale

    pass
