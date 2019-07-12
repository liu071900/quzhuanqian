import peewee
from .base import BaseModel
from datetime import datetime


class User(BaseModel):
    """
        基础 用户表
        需要加 微信登陆 字段
    """
    # 唯一标识符
    user_id = peewee.IntegerField(null=False, unique=True, index=True)
    # 用户名称 默认是手机号
    user_name = peewee.CharField(max_length=128, null=False)
    # 用户头像
    avatar = peewee.CharField(max_length=128, null=True, default='default')
    # 用户手机，用于登录账号
    phone = peewee.CharField(max_length=11, unique=True, index=True, null=False, default=None)
    # 用户密码
    password = peewee.CharField(max_length=255, null=False)
    # 加入日期
    join_date = peewee.DateField(index=True, default=datetime.today())
    # 用户等级
    user_level = peewee.IntegerField(default=0)
    # 微信账号，用于提现
    w_account = peewee.CharField(max_length=256, null=True)
    # 支付宝账号，用于提现
    z_account = peewee.CharField(max_length=256, null=True)
    # 一级邀请人
    inviter1 = peewee.IntegerField(null=True, default=0)
    # 二级邀请人
    inviter2 = peewee.IntegerField(null=True, default=0)
    is_active = peewee.BooleanField(default=True)
    
    class Meta:
        table_name = 'base_user'


class Group(BaseModel):
    """
        社区表
    """
    # 社区id,官方社区id为0
    group_id = peewee.AutoField(primary_key=True)
    # 社区名称
    group_name = peewee.CharField(max_length=256, null=False)
    owner = peewee.ForeignKeyField(model=User, field='user_id')
    is_active = peewee.BooleanField(default=True)

    class Meta:
        table_name = 'base_group'


class UserGroup(BaseModel):
    """
        用户组，关系表
    """
    user = peewee.ForeignKeyField(model=User, field="user_id")
    group = peewee.ForeignKeyField(model=Group, field="group_id")

    class Meta:
        table_name = 'base_user_group'


