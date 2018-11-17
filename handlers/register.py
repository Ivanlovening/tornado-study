#encoding=utf-8
#version:python3.6.0
#Tools:PyCharm 2017.3.2
#Author:yinfei
#Email:1073477805@qq.com

"""
用户注册
"""

import tornado.web
import methods.readdb as mrb
import methods.writedb as mwb

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("register.html")

    def post(self):
        username = self.get_argument('username')
        email = self.get_argument('email')
        password = self.get_argument('password')
        confirm_password = self.get_argument('confirm_password')
        if password!=confirm_password:
            self.write('两次密码不一致')
        else:
            columns = "(%s,%s,%s)"%("username","email","password")
            values = "('%s','%s','%s')"%(username,email,password)
            result = mwb.insert_table("users",columns,values)

            user_infos = mrb.select_table(table="users", column="*", condition="username", value=username)
            if user_infos:
                self.write("账号已经注册！")
            else:
                if result:
                    self.write('1')
                else:
                    self.write("注册失败！")
