#encoding=utf-8
#version:python3.6.0
#Tools:PyCharm 2017.3.2
#Author:yinfei
#Email:1073477805@qq.com

"""
数据库写操作
"""
from methods.db import *

def insert_table(table,columns,values):
    sql = "insert into " + table + " " + columns + " values " + values
    mycursor.execute(sql)
    mydb.commit()
    return mycursor.rowcount