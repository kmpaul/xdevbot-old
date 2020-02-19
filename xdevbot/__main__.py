import sys

from .main import main

# Read default_map from config files with ConfigParser
default_map = {}

main(sys.argv[1:], prog_name='xdevbot', auto_envvar_prefix='XDEV', default_map=default_map)
