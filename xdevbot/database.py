import motor.motor_asyncio


async def init_db(app):
    if app['config']['mongodb']:
        uri = app['config']['mongodb']
        db = motor.motor_asyncio.AsyncIOMotorClient(uri, io_loop=app.loop).boards
    else:
        db = None
    app['db'] = db


async def close_db(app):
    pass
