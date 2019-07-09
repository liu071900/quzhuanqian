"""
    http 处理类 的基类，
    后续所有的通用处理 必须继承 BaseApiHandler 或者 BaseViewHandler

"""

import json
from tornado.web import RequestHandler,HTTPError
from tornado.web import authenticated
import asyncio
from exceptions import ResultCode

from typing import Union

class User(object):

    def __init__(self):
        pass
    

class AnonymousUser():
    """
        匿名用户
    """
    def __init__(self):
        pass


class BaseApiHandler(RequestHandler):
    """
        api接口处理类
    """
    def initialize(self):

        # application 简写
        self.app = self.application

        # 数据库对象,可直接操作数据库。来自peewee_async Manager()对象
        self.db_objects = self.application.db_manager

        # 如果存在以下情况，某个查询需要优先从缓存中获取，或者 可复用的查询，封装到 service模块下
        self.db_service = None
        
    async def prepare(self):
        # 1.连接数据库
        await self.db_service.connect()
        # 

    def get_current_user(self):
        """
            基于cookie 获取当前的用户,程序中通过 self.current_user 访问 user对象
        """
        cookie_user = self.get_secure_cookie("sessionId")

        print('cookie_user',cookie_user)
        # sessionId userId+";"+ expire
        return cookie_user

    def get_json_body(self):
        """
            获取body参数，转换为dict,如果发生异常，抛出错误
        """
        body = self.request.body
        try:
            json_data = json.loads(body)
        except:
            json_data = None
            raise HTTPError(status_code=501, reason="请求body,格式不正确")
        return json_data
    
    def respond_json(self,response:Union[dict,list],code:str = ResultCode.SUCCESS,message:str =''):
        """
            封装 self.write, 统一的 json response 返回处理
        """
        if not isinstance(response,(dict,list,)):
            raise Exception("responde 必须为字典对象")
            
        result = {"code":code,"message":message,"data":response}
        self.write(result)

    def on_finish(self):
        """
            请求结束时候回调函数
        """
        status = self.get_status()
        # TODO 状态码 大于500 需要记录
        print(status)       
        # 本次请求的时间
        print(self.request.request_time())

        loop = asyncio.get_event_loop()
        loop.create_task(self.db_objects.close())


class BaseViewHandler(RequestHandler):
    """
        返回页面的处理 基类
    """


