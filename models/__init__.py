"""
    orm 模型，数据库表命名规则如下：
    1.非基础表加命令空间前缀，如 auth_invitation,base_group_config
    2.表名 全部为小写字符，
    
    文件分类，根据功能模块，一个模块建立一个 model文件
"""


from .base import UserId,GroupId
from .user import User,Group,UserGroup



