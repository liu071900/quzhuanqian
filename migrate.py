"""
    创建数据的 脚本,peewee 没有django那么智能，改动model后，需要删除对应的表从新 运行下脚本不然，不会改动数据库表结构
"""

import models
import peewee

attrs_list = dir(models)
tables:list = list()

for attr in attrs_list:
    m = getattr(models,attr)
    if isinstance(m,peewee.ModelBase):
        tables.append(m)

from settings import DATA_BASE


DATA_BASE.create_tables(tables)

#初始化 InvitationCode

DATA_BASE.close()
