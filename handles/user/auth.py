"""
    用户认证接口
"""
import re
from tornado.web import HTTPError
from handles.base import BaseApiHandler

from peewee import DoesNotExist
from models.user import User
from services import VerifyCodeTypes

from exceptions import ResultCode


class SignupHandler(BaseApiHandler):
    """
        注册处理
    """
    def get(self):
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
        verification_code = payload["verification_code"]
        inviter_code = payload.get("inviter_code", None)
        # TODO 合法性校验
        code, message = await self.check_validity(phone, password, str(verification_code), inviter_code)
        if not code == ResultCode.SUCCESS:
            return self.respond_json({}, code=code, message=message)

        user_id = await self.service.user.make_user_id()
        inviter1 = inviter_code if inviter_code else 0
        inviter2 = await self.get_inviter2(inviter_code)

        user_info = dict(user_id=user_id, user_name='用户-' + str(phone), phone=phone,
                         password=SignupHandler.make_password(password), inviter1=inviter1, inviter2=inviter2)
        user = User(**user_info)
        ret = await self.service.user.create_user(user)
        if not ret:
            code = ResultCode.SIG_IN_ERROR
            message = "database error"
        self.respond_json({}, code=code, message=message)

    async def check_validity(self, phone: str, password: str, verification_code: str, inviter_code:int = None) -> tuple:
        """
            合法性校验,
            return (code,message)
        """
        # TODO 完善以下功能
        code = ResultCode.SUCCESS
        message = '注册成功'
        # 1.校验手机号格式
        ret = re.match(r"^1[35678]\d{9}$", str(phone))
        if not ret:
            code = ResultCode.join_code(ResultCode.SIG_IN_ERROR, '1')
            message = "手机号不正确"
            return code, message

        # 2.校验密码
        if not password:
            code = ResultCode.join_code(ResultCode.SIG_IN_ERROR, '2')
            message = "密码不能为空"
            return code, message

        # 3.校验 验证码
        ret = await self.service.user.auth_verification_code(VerifyCodeTypes.SIG_IN, verification_code)
        if not ret:
            code = ResultCode.join_code(ResultCode.SIG_IN_ERROR, '3')
            message = "验证码不正确"
            return code, message

        # 4.校验邀请码，如果有邀请码，则邀请码必须有效，邀请码为用户的id
        if inviter_code:
            try:
                await self.db_objects.execute(User.select().where(User.user_id == inviter_code))
            except DoesNotExist:
                code = ResultCode.join_code(ResultCode.SIG_IN_ERROR, '5')
                message = "重复注册"
                return code, message

        # 5.用户是否已经注册
        get_user = None
        try:
            get_user = await self.db_objects.execute(User.select().where(User.phone == phone))
        except DoesNotExist:
            pass
        if get_user:
            code = ResultCode.join_code(ResultCode.SIG_IN_ERROR, '5')
            message = "用户已经注册"
            return code, message

        return code, message

    @staticmethod
    def make_password(raw: str)->str:
        # TODO 加密密码
        return raw

    async def get_inviter2(self, inviter_code):
        if inviter_code:
            try:
                user = await self.db_objects.get(User, user_id=inviter_code)
                return user.inviter1
            except DoesNotExist:
                return 0
        else:
            return 0


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