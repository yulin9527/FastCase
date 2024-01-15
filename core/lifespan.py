import asyncio
from tortoise import Tortoise


class Lifespan(object):
    def __init__(self):
        self.loop = asyncio.get_event_loop()

    def __enter__(self):
        self.loop.run_until_complete(self.__life_start())
        print('开始执行')
        return self.loop

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.loop.run_until_complete(self.__life_stop())
        print('执行结束')

    def __del__(self):
        self.loop.close()

    @staticmethod
    async def __life_start():
        await Tortoise.init(
            db_url='sqlite://db.sqlite3',
            modules={'models': ['core.models']}
        )
        await Tortoise.generate_schemas()

    @staticmethod
    async def __life_stop():
        await Tortoise.close_connections()
