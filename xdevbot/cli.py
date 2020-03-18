import logging
from configparser import ConfigParser

import aiohttp_jinja2
import click
import jinja2
from aiohttp import web

from .database import close_db, init_db
from .middlewares import setup_middlewares
from .routes import setup_routes

DEFAULT_CONFIG_PATHS = ['config.ini']


async def init_app(config=None):
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader(__package__, 'templates'))

    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)

    setup_routes(app)
    setup_middlewares(app)

    return app


def config_callback(ctx, config_param, config_file):
    config_paths = DEFAULT_CONFIG_PATHS + ([config_file] if config_file else [])
    cfgparser = ConfigParser()
    cfgparser.read(config_paths)
    config = dict(cfgparser[__package__]) if __package__ in cfgparser else dict()
    for param in ctx.command.params:
        if param.name in config:
            param.default = config[param.name]


@click.command()
@click.version_option(prog_name='Xdev Bot', version='0.0.1')
@click.option('--host', default=None, type=str, help='Server IP address')
@click.option('--port', default=None, type=int, help='Server port number')
@click.option('--logging', default=logging.INFO, help='Logging output level')
@click.option('--mongodb', default=None, type=str, help='MongoDB URI')
@click.option(
    '--config',
    default=None,
    type=click.Path(exists=True),
    help='User-defined configuration file location',
    is_eager=True,
    expose_value=False,
    callback=config_callback,
)
def cli(**config):
    logging.basicConfig(level=config['logging'])
    app = init_app(config=config)
    web.run_app(app, host=config['host'], port=config['port'])
