import logging

import pytest
from mockupdb import MockupDB


@pytest.fixture
def cli_env(monkeypatch):
    monkeypatch.setenv('APP_HOST', 'http://127.0.0.1')
    monkeypatch.setenv('APP_PORT', '6789')
    monkeypatch.setenv('LOGGING', str(logging.CRITICAL))


@pytest.fixture
def cli_configfile(tmpdir):
    f = tmpdir.mkdir('config').join('config.ini')
    f.write(
        """[app]
host = http://0.0.0.0
port = 9999
"""
    )
    return f


@pytest.yield_fixture
def mockdbserver(loop):
    server = MockupDB()
    server.run()
    yield server
    server.stop()
