#encoding=gbk
#version:python3.6.0
#Tools:PyCharm 2017.3.2
#Author:yinfei
#Email:1073477805@qq.com
"""
首页
"""
import tornado.web
import methods.readdb as mrd
from handlers.base import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)

        if user_infos:
            pwd = user_infos[0][2]
            if pwd == password:
                self.set_current_user(username)
                self.write(username)
            else:
                self.write("密码错误")
        else:
            self.write("没有该用户")

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user',tornado.escape.json_encode(user))  # 注意这里使用了tornado.escape.json_encode()方法
        else:
            self.clear_cookie("user")

class ErrorHandler(BaseHandler):  # 增加了一个专门用来显示错误的页面
    def get(self):  # 但是后面不单独讲述，读者可以从源码中理解
        self.render("error.html")