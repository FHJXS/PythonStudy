# -*- coding: UTF-8 -*-
'''
Created on 2018��2��10��

@author: www60
'''
import re


def func1():
    """
A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
^表示行的开头，^\d表示必须以数字开头。
$表示行的结束，\d$表示必须以数字结束。
    """
    m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
    print(m)
    print(m.group(0))  # 匹配整个字符串
    print(m.group(1))  # 按照区域切割获取字符串
    print(m.group(2))
    print(re.split(r'\s+', 'a b   c'))
    print(re.split(r'[\s\,]+', 'a,b, c  d'))
    print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
    pass


def test():
    func1()
    pass


if __name__ == '__main__':
    test()
    pass
