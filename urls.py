"""
    app 全部的路由表
"""

from handles.user import auth


routes = [
    # 1. 用户处理
    # 1.1 注册
    (r'/signup',auth.SignupHandler),

    # 1.2 登陆
    (r'/login',auth.LoginHandler),
    
    
]