#encoding=utf-8
#version:python3.6.0
#Tools:PyCharm 2017.3.2
#Author:yinfei
#Email:1073477805@qq.com

"""
配置项目文件
"""
from url import url

import tornado.web
import os

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__),"templates"),
    static_path = os.path.join(os.path.dirname(__file__),"statics"),
    cookie_secret = "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    xsrf_cookies = True,
    debug = True,   #调试模型，修改后自动更新
    login_url = '/',#没登录自动跳转地址
)

application = tornado.web.Application(
    handlers = url,
    **settings
)