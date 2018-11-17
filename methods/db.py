#encoding=utf-8
#version:python3.6.0
#Tools:PyCharm 2017.3.2
#Author:yinfei
#Email:1073477805@qq.com
import mysql.connector as mysql

#连接mysql  （连接对象）
mydb = mysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    database='python'
)

#获取mysql指针对象，进行mysql各种操作都是使用这个指针对象的各个方法。
mycursor = mydb.cursor()