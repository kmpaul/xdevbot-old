import logging

import pytest


@pytest.fixture
def cli_env(monkeypatch):
    monkeypatch.setenv('XDEV_HOST', 'http://127.0.0.1')
    monkeypatch.setenv('XDEV_PORT', '6789')
    monkeypatch.setenv('LOGGING', str(logging.CRITICAL))


@pytest.fixture
def cli_configfile(tmpdir):
    f = tmpdir.mkdir('config').join('config.ini')
    f.write(
        """[xdevbot]
host = http://0.0.0.0
port = 9999
"""
    )
    return f
