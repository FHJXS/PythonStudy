# -*- coding: utf-8 -*-
# 导入MySQL驱动:
import pymysql
import cx_Oracle as oracle

def DBconnection():
    # 注意把password设为你的root口令:
    conn = pymysql.connect(host="127.0.0.1",user="root",password="1234",database="tb_test",port=3306,charset="utf8")
    cursor = conn.cursor()
    #查询
    cursor.execute("select * from tb_book WHERE book_num = %d"%(1))
    result = cursor.fetchall()
    for i in result:
        print(i)
    # print(result)
    cursor.close()
    conn.close()

def oraclefunc():
    """
    连接Oracle数据库
    :return:
    """
    conn = oracle.connect("mkt_develop/mkt_develop@192.168.1.146:1521/orcl")
    cursor = conn.cursor()

    cursor.execute('select sysdate from dual')

    data = cursor.fetchone()

    print(data)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    """
    执行INSERT等操作后要调用commit()提交事务；
    MySQL的SQL占位符是%s。
    """
    # DBconnection()
    oraclefunc()