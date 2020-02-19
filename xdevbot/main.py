import logging

import aiohttp_jinja2
import click
import jinja2
from aiohttp import web

from .middlewares import setup_middlewares
from .routes import setup_routes


async def init_app(config=None):

    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('xdevbot', 'templates'))

    # app.on_startup.append(load_db)
    # app.on_cleanup.append(save_db)

    setup_routes(app)
    setup_middlewares(app)

    return app


@click.command()
@click.version_option(prog_name='Xdev Bot', version='0.0.1')
@click.option('--host', default=None, type=str, help='Server IP address')
@click.option('--port', default=None, type=int, help='Server port number')
@click.option('--logging', default=logging.INFO, help='Logging output level')
def main(**config):
    print(config)
    logging.basicConfig(level=config['logging'])
    app = init_app(config=config)
    web.run_app(app, host=config['host'], port=config['port'])
