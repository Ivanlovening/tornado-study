#encoding=gbk
#version:python3.6.0
#Tools:PyCharm 2017.3.2
#Author:yinfei
#Email:1073477805@qq.com
"""
��ҳ
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
                self.write("�������")
        else:
            self.write("û�и��û�")

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user',tornado.escape.json_encode(user))  # ע������ʹ����tornado.escape.json_encode()����
        else:
            self.clear_cookie("user")

class ErrorHandler(BaseHandler):  # ������һ��ר��������ʾ�����ҳ��
    def get(self):  # ���Ǻ��治�������������߿��Դ�Դ�������
        self.render("error.html")