"""
    用户相关的数据库操作
"""
from .base import DbService
from peewee_async import Manager
from models.user import User


class UserService(DbService):

    def __init__(self,db:Manager):
        super(UserService).__init__(self,db)

        return self
    
    @classmethod
    async def create_user(cls,db:Manager, user:User):
        """
            创建一个用户，参数为一个user,这个服务 只更新 user_id字段
        """
        assert isinstance(user,User),'user 必须一个 User model的实例'
        user_id = await db.create()
        

        return 1


