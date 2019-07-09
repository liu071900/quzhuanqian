import asyncio
from tornado import web
from tornado import ioloop
from tornado import locks
from tornado.platform.asyncio import AsyncIOMainLoop
from tornado.options import options,define


from urls import routes
from settings import app_settings,DATA_BASE

from peewee_async import Manager

options.define('port',default=8000,type=int,help="监听的端口号")


class App(web.Application):
    def __init__(self) -> None:
        super(App,self).__init__(routes, 
        default_host = None,
        transforms=None,
        **app_settings)
    def setup_db_manager(self,db_manager):
        """
            引入 peewee-async 的 Manager 
        """
        self.db_manager = db_manager

def main(port:int= None) ->None:
    # 必须明确指出 使用 asyncio 事件循环，不知道是不是 只有windows下才需要明确指出
    AsyncIOMainLoop().install()
    loop = asyncio.get_event_loop()
    #print(dir(loop))
    app = App()
    db_manager = Manager(database=DATA_BASE,loop =loop)
    db_manager.database.allow_sync = False
    app.setup_db_manager(db_manager)

    # TODO 生产环境不能这么做
    app.listen(options.port)
    loop.call_soon(lambda:print(f'server had started at {options.port}'))
    loop.run_forever()
    # 这里简单 以ctrl+c 处理退出
    # 生产环境 需要处理 优雅退出问题
    # 参考https://www.keakon.net/2012/12/17/%E7%94%9F%E4%BA%A7%E7%8E%AF%E5%A2%83%E4%B8%8B%E5%A6%82%E4%BD%95%E4%BC%98%E9%9B%85%E5%9C%B0%E9%87%8D%E5%90%AFTornado

    # shutdown_event = locks.Event()
    # await shutdown_event.wait()


if __name__ == "__main__":

    # TODO 生产环境不能这么搞
    main()
    
