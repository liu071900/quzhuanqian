"""
    用户相关的数据库操作
"""
import asyncio
from typing import Union
from .base import BaseDbService
from models.user import User, UserGroup,Group
from models.base import UserId
from peewee import DoesNotExist, IntegrityError
from peewee_async import Manager
from datetime import datetime


class UserService(BaseDbService):

    async def create_user(self, user: User)-> int:
        """
            新创建一个用户，向base_user表插入一条数据，开启事务
        """
        assert isinstance(user, User), "user 必须是User的实例"

        async def _task(db: Manager)->int:
            async with db.atomic():
                # 向 user表插入一条数据，返回值是pk
                pk = await db.execute(user.insert(user.__data__))
                # 添加默认社区
                # 1. 加入官方社区
                group = await db.get(Group, group_id=1)
                await db.create(UserGroup, user=user, group=group)
                # 2.加入一级邀请人的社区
                if user.inviter1:
                    try:
                        group2 = await db.get(Group, owner=user.inviter1)
                        await db.create(UserGroup, user=user, group=group2)
                    except DoesNotExist:
                        pass
                    except IntegrityError:
                        raise IntegrityError
            return pk

        loop = asyncio.get_event_loop()
        result = await loop.create_task(_task(self.db))
        return result

    async def make_user_id(self) ->int:
        """
            生成一个全局唯一的user_id
        """
        user_id = await self.db.execute(UserId().insert())
        return user_id

    async def auth_verification_code(self,type:int, code: str,)-> bool:
        """
            验证码校验，可能要去redis中取数据
        :return:
        """
        # TODO 接口待完成
        return True
