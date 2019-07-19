import os
from aiohttp import web

port = os.environ.get('PORT', 8080)
routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")


app = web.Application()
app.add_routes(routes)
web.run_app(app, port=port)
