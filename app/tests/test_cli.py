import logging

from app.cli import DEFAULT_CONFIG, cli


def test_cli_defaults():
    ctx = cli.make_context(cli.name, args=[], auto_envvar_prefix='APP')
    assert ctx.params == DEFAULT_CONFIG


def test_cli_host():
    params = {'host': 'http://localhost', 'port': None, 'logging': logging.INFO, 'mongodb': None}
    ctx = cli.make_context(cli.name, args=['--host', params['host']], auto_envvar_prefix='APP')
    assert ctx.params == params


def test_cli_port():
    params = {'host': None, 'port': 4567, 'logging': logging.INFO, 'mongodb': None}
    ctx = cli.make_context(cli.name, args=['--port', str(params['port'])], auto_envvar_prefix='APP')
    assert ctx.params == params


def test_cli_logging():
    params = {'host': None, 'port': None, 'logging': logging.WARNING, 'mongodb': None}
    ctx = cli.make_context(
        cli.name, args=['--logging', str(params['logging'])], auto_envvar_prefix='APP'
    )
    assert ctx.params == params


def test_cli_mongodb():
    params = {
        'host': None,
        'port': None,
        'logging': logging.INFO,
        'mongodb': 'mongodb://test.mongodb.com',
    }
    ctx = cli.make_context(
        cli.name, args=['--mongodb', params['mongodb']], auto_envvar_prefix='APP'
    )
    assert ctx.params == params


def test_cli_env(cli_env):
    params = {'host': 'http://127.0.0.1', 'port': 6789, 'logging': logging.INFO, 'mongodb': None}
    ctx = cli.make_context(cli.name, args=[], auto_envvar_prefix='APP')
    assert ctx.params == params


def test_cli_env_overridden(cli_env):
    params = {'host': 'http://127.0.0.1', 'port': 9999, 'logging': logging.INFO, 'mongodb': None}
    ctx = cli.make_context(cli.name, args=['--port', str(params['port'])], auto_envvar_prefix='APP')
    assert ctx.params == params


def test_cli_configfile(cli_configfile):
    params = {'host': 'http://0.0.0.0', 'port': 9999, 'logging': logging.INFO, 'mongodb': None}
    ctx = cli.make_context(cli.name, args=['--config', cli_configfile], auto_envvar_prefix='APP')
    assert ctx.params == params


def test_cli_configfile_overridden(cli_configfile):
    params = {'host': 'http://0.0.0.0', 'port': 8888, 'logging': logging.INFO, 'mongodb': None}
    ctx = cli.make_context(
        cli.name,
        args=['--config', cli_configfile, '--port', str(params['port'])],
        auto_envvar_prefix='APP',
    )
    assert ctx.params == params


def test_cli_env_configfile_overridden(cli_env, cli_configfile):
    params = {'host': 'http://127.0.0.1', 'port': 8888, 'logging': logging.INFO, 'mongodb': None}
    ctx = cli.make_context(
        cli.name,
        args=['--config', cli_configfile, '--port', str(params['port'])],
        auto_envvar_prefix='APP',
    )
    assert ctx.params == params
