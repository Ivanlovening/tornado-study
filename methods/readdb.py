#encoding=utf-8
#version:python3.6.0
#Tools:PyCharm 2017.3.2
#Author:yinfei
#Email:1073477805@qq.com
"""
数据库读操作
"""
from methods.db import *

def select_table(table,column,condition,value):
    sql = "select "+column+" from "+table+" where "+condition+"='"+value+"'"
    mycursor.execute(sql)
    lines = mycursor.fetchall()
    return lines

def select_columns(table,column):
    sql = "select " + column + " from " + table
    mycursor.execute(sql)
    values = mycursor.fetchall()
    return values

