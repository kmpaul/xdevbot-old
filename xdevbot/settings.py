from configparser import ConfigParser

_CONFIG_FILES = ['setup.cfg']

_config_parser = ConfigParser(default_section='xdevbot')
_config_parser.read(_CONFIG_FILES)

config = dict(_config_parser.items('xdevbot'))
