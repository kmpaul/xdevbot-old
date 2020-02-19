import sys

from .main import main

main(sys.argv[1:], prog_name='xdevbot', auto_envvar_prefix='XDEV', default_map={})
