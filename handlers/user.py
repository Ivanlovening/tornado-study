#encoding=utf-8
#version:python3.6.0
#Tools:PyCharm 2017.3.2
#Author:yinfei
#Email:1073477805@qq.com
"""
用户信息
"""
import tornado.web
import methods.readdb as mrd
from handlers.base import BaseHandler

class UserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = tornado.escape.json_decode(self.get_current_user())
        user_infos = mrd.select_table(table="users", column="*", condition="username", value=username)

        self.render("user.html",users=user_infos)