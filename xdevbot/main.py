import logging

import aiohttp_jinja2
import click
import jinja2
from aiohttp import web

from .middlewares import setup_middlewares
from .routes import setup_routes
from .settings import CommandWithConfig, get_config


async def init_app(config=None):

    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('xdevbot', 'templates'))

    # app.on_startup.append(load_db)
    # app.on_cleanup.append(save_db)

    setup_routes(app)
    setup_middlewares(app)

    return app


@click.command(cls=CommandWithConfig)
def main(**kwargs):
    config = get_config(**kwargs)
    logging.basicConfig(level=config['logging'])
    app = init_app(config=config)
    web.run_app(app, host=config['host'], port=config['port'])
