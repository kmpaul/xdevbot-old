import sys

from .cli import cli

cli(sys.argv[1:], prog_name='xdevbot', auto_envvar_prefix='XDEV')
