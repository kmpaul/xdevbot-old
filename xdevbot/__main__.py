import sys

from .cli import cli
from .settings import config

cli(sys.argv[1:], prog_name='xdevbot', auto_envvar_prefix='XDEV', default_map=config)
