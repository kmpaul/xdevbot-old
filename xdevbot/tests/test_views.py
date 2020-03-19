from xdevbot.cli import init_app


async def test_index(aiohttp_client, loop):
    app = await init_app()
    client = await aiohttp_client(app)
    resp = await client.get('/')
    assert resp.status == 200
    text = await resp.text()
    assert text == 'Hello Aiohttp!'
