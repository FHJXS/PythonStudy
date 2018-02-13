# -*- coding: utf-8 -*-
'''
Created on 2018年2月5日17:16:34

@author: www60
'''
import os
import sys  # 导包


def main():
#     a = 1
#     print("Hello{tip}".format(tip="World"))
#     b = input("\n\n按下 enter 键后退出。")
#     print(b + "\n" + str(a))
    a, b = 2, 3
#     c, d = "ab"
#     print(c + "\n" + d)
#     if a + b > c + d :
#         print("不可能的")
#     else:
#         print("绝对的")
    print("本程序的进程 PID = " + str(os.getpid()))
    print(os.listdir("/"))
    if a > b:
        print("True")
    elif a < b:
        print("False")        
    else:
        x = "测试信息"
        sys.stdout.write(x + "\n")  # 多行输出

    # 输出不换行
    print(a, end=" ")
    
#     print("命令行参数为:")
#     for i in sys.argv:
#         print(i)
#     print("\n Python 路径为：", sys.path)


""" 
这里是注释信息
"""
if __name__ == '__main__':
    main()
