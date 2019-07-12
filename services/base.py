"""

"""

from peewee_async import Manager


class BaseDbService:
    """
        类装饰器
    """
    def __init__(self, db: Manager)->None:
        assert isinstance(db, Manager), '参数 db 必须一个 peewee_async.Manager的实例'
        self.db = db

    def set_db(self, db):
        assert isinstance(db, Manager), '参数 db 必须一个 peewee_async.Manager的实例'
        self.db = db

