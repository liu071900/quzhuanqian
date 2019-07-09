import peewee
import peewee_async

from typing import Mapping


# 数据配置，http://docs.peewee-orm.com/en/latest/peewee/database.html
# https://peewee-async.readthedocs.io/en/latest/peewee_async/api.html
DATA_BASE = peewee_async.MySQLDatabase("app",host="127.0.0.1",user="root",password="root",port=3306)

app_settings:Mapping = dict(
            blog_title=u"Tornado Blog",
            xsrf_cookies=False,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            debug=True,
            autoreload=True
        )

