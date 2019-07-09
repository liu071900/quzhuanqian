"""
    一些实例代码
"""

import asyncio

from peewee_async import Manager
from settings import app_settings,DATA_BASE
from models import UserId
from peewee import IntegrityError
import random
import peewee

loop = asyncio.get_event_loop()
db_manager = Manager(database=DATA_BASE,loop =loop)
db_manager.database.allow_sync = False
# InvitationCode 生成一些数据

class InvitationCode(peewee.Model):
    """
        用户邀请码，需要事先生成，邀请码为6位随机数，邀请码同时作为userId
    """
    code = peewee.IntegerField(unique=True,null=False)
    is_used = peewee.BooleanField(index=True,default=False)
    
    class Meta:
        database = DATA_BASE


async def init_table_invitationCode():
    
    await db_manager.connect()
    creat_count = 100
    i = 0
    start = loop.time()

    # 这里演示 事物的使用方法，实际运行中，必须将事物包裹到 task中，不然可能出现不可预测的错误
    # https://peewee-async.readthedocs.io/en/stable/peewee_async/tornado.html
    async with db_manager.atomic():
        while i<creat_count:
            i+=1
            code = random.randint(10000,999999)
            try:
                # 返回值是 新插入数据的 pk
                uid = await db_manager.create(UserId)
            except IntegrityError:
                continue
    
    await db_manager.close()
    end = loop.time()
    print(end -start)
if __name__ == "__main__":
    loop.run_until_complete(init_table_invitationCode())    