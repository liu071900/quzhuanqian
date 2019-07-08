"""
    用户认证接口
"""
from tornado.web import HTTPError
from handles.base import BaseApiHandler

from peewee import DoesNotExist
from models.user import User

from exceptions import ResultCode

class SignupHandler(BaseApiHandler):
    """
        注册处理
    """
    def get(sllf):
        """
            返回 注册界面
        """
        pass

    async def post(self):
        """
            注册
        """
        payload = self.get_json_body()
        phone = payload["phone"]
        password = payload["password"]
        verifity_code = payload["verifity_code"]
        inviter_code = payload.get("inviter_code",None)
        # TODO 合法性校验
        code,message = await self.check_invild(phone,password,verifity_code,inviter_code)
        if not code == ResultCode.SUCCESS:
            return self.respond_json({},code=code,message=message)
        # 生成一个 user
        

        # 3.加入默认社区
        self.respond_json({})

    async def check_invild(self,phone:int,password:str,verifity_code:int,inviter_code:int = None) -> tuple:
        """
            合法性校验,
            return (code,message)
        """
        # TODO 完善以下功能
        code = ResultCode.SUCCESS
        message = '注册成功'
        # 1.校验手机号格式
        # 2.校验密码
        # 3.校验 验证码
        # 4.校验邀请码，如果有邀请码，则邀请码必须有效，邀请码为用户的id
        # 5.用户是否已经注册
        # get_user = None
        # try:
        #     get_user = self.db_objects.get(User.select().where(User.phone==phone))
        # except DoesNotExist:
        #     pass
        # if get_user:
        #     code = ResultCode.join_code(ResultCode.SIGIN_ERROR,'5')
        #     message = "用户已经注册" 
        #     return (code,message)

        return (code,message)
        

class LoginHandler(BaseApiHandler):
    """
        登陆处理
    """
    def get(self):
        pass

    def post(self):    
        """
            登陆处理
        """
        data = self.get_json_body()
        
        print(data)
        print(self.current_user)
        
        self.write('post')