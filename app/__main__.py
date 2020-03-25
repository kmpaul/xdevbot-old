import sys

from .cli import cli

cli(sys.argv[1:], prog_name='app', auto_envvar_prefix='APP')
