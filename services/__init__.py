"""
    这个模块封装连接到 第三方服务的操作，包括 数据库 redis,等外部程序
    如果需要缓存的查询，封装到这个模块来
"""

from .user import UserService
from peewee_async import Manager


class VerifyCodeTypes:
    SIG_IN = 1


class Service:
    """
        集合了所有的service
    """
    def __init__(self, db: Manager):
        assert isinstance(db, Manager), '参数 db 必须一个 peewee_async.Manager的实例'
        # user_service
        self.user = UserService(db)

