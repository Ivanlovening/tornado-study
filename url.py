#encoding=utf-8
#version:python3.6.0
#Tools:PyCharm 2017.3.2
#Author:yinfei
#Email:1073477805@qq.com

"""
网站的url
"""

from handlers.index import IndexHandler
from handlers.user import UserHandler
from handlers.register import RegisterHandler

url = [
    (r'/',IndexHandler),
    (r'/user',UserHandler),
    (r'/register',RegisterHandler)
]