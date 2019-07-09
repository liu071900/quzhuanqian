import peewee
from datetime import datetime
from settings import DATA_BASE

# 数据配置，http://docs.peewee-orm.com/en/latest/peewee/database.html
#database = peewee.MySQLDatabase(None)
# when run set: database.init(database_name, host='localhost', user='mysql')

class BaseModel(peewee.Model):
    """
        基础模型，所有的模型需要继承此模型
    """
    create_time = peewee.DateTimeField(default=datetime.now())
    update_time = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = DATA_BASE



class UserId(peewee.Model):
    """
        用于生成 用户id，同时也作为用户的专属邀请码，为了保证邀请码大于等于5位数，程序部署前需要事先准备预留数据
        注意：这里只是用作生成 用户id，但不代表每个id 都是有效用户
    """
    # 主键
    uid = peewee.AutoField()
    create_time = peewee.DateTimeField(default=datetime.now())
    class Meta:
        database = DATA_BASE

class GroupId(peewee.Model):
    """
        用于生成 社区id，社区id，原理同 UserId 程序部署前需要事先准备预留数据
    """
    # 主键
    uid = peewee.AutoField()
    create_time = peewee.DateTimeField(default=datetime.now())
    class Meta:
        database = DATA_BASE

class Session(peewee.Model):
    """
        session表
    """
    pass