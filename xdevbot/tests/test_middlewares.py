from aiohttp import web

from xdevbot.cli import init_app


async def test_404(aiohttp_client, loop):
    app = await init_app()
    client = await aiohttp_client(app)
    resp = await client.get('*&!@#$%')
    assert resp.status == 200


async def test_500(aiohttp_client, loop):
    app = await init_app()

    async def error(request):
        raise web.HTTPInternalServerError()

    app.router.add_get('/error', error)

    client = await aiohttp_client(app)
    resp = await client.get('/error')
    assert resp.status == 200
