import re

"""
预定义字符类 
. 任何字符（与行结束符可能匹配也可能不匹配） 
\d 数字：[0-9] 
\D 非数字： [^0-9] 
\s 空白字符：[ \t\n\x0B\f\r] 
\S 非空白字符：[^\s] 
\w 单词字符：[a-zA-Z_0-9] 
\W 非单词字符：[^\w] 

Greedy 数量词 
X? X，一次或一次也没有 
X* X，零次或多次 
X+ X，一次或多次 
X{n} X，恰好 n 次 
X{n,} X，至少 n 次 
X{n,m} X，至少 n 次，但是不超过 m 次 
"""


def func():
    test = input(r"请输入字符串：")
    if re.match(r'\w', test):
        print("ok")
    else:
        print("failed")

    pass

def func2():
    #group(0)永远是原始字符串
    t = '19:05:30'
    m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',t)
    print(m.groups())
    #正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
    print(re.match(r'^(\d+)(0*)$', '102300').groups())
    #非贪婪匹配 加个?就可以让\d+采用非贪婪匹配
    print(re.match(r'^(\d+?)(0*)$', '102300').groups())

def func3():
    """
    如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式
    :return: None
    """
    # 编译:
    re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
    # 使用：
    print(re_telephone.match('010-12345').groups())
    print(re_telephone.match('010-8086').groups())
def name_of_email(addr):
    m = re.compile(r'^(\w*)(@\w*)([.\w*]*)')
    return m.match(addr)

if __name__ == '__main__':
    # func()
    # 测试:
    # assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
    # assert name_of_email('tom@voyager.org') == 'tom'
    print(name_of_email('tom@voyager.org.cn').groups())
    func2()
    func3()