# -*- coding: utf-8 -*-
'''
Created on 2018��2��9��

@author: www60
'''
"""
代码解读：
        对Pool对象调用join()方法会等待所有子进程执行完毕，
        调用join()之前必须先调用close()，调用close()之
        后就不能继续添加新的Process了
"""
from multiprocessing import Pool
import os
import random
import subprocess
import time


def long_time_task(name):
    print('运行实例  %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('此实例  %s 运行  %0.2f 秒.' % (name, (end - start)))
#     print('$ nslookup www.python.org')
#     # subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
#     r = subprocess.call(['nslookup', 'www.python.org'])
#     print('Exit code:', r)
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 子进程还需要输入，则可以通过communicate()方法输入
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print(err.decode('utf-8'))
    print('Exit code:', p.returncode)


if __name__ == '__main__':
    print('父线程 PID ： %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('等待所有子进程完成...')
    p.close()
    p.join()
    print('所有子进程完成.')
