from configparser import ConfigParser

from click import Command, Option, Path

DEFAULT_CONFIG_PATHS = ['setup.cfg']


def config_command(config_param='config', config_section=None):
    class ConfigCommand(Command):
        def __init__(self, **kwargs):
            config_option = Option(
                [f'--{config_param}'],
                default=None,
                type=Path(exists=True),
                help='User-defined configuration file location',
            )
            if 'params' in kwargs:
                kwargs['params'].append(config_option)
            else:
                kwargs['params'] = [config_option]

            super().__init__(**kwargs)

        def invoke(self, ctx):
            user_config = ctx.params[config_param]
            config_paths = DEFAULT_CONFIG_PATHS.copy()
            if user_config is not None:
                config_paths.append(user_config)
            cfgparser = ConfigParser()
            cfgparser.read(config_paths)
            config = dict(cfgparser[config_section].items())
            for param, value in ctx.params.items():
                if param in config:
                    ctx.params[param] = config[param]
                    print(f'{param}: {value} --> {config[param]}')
                else:
                    print(f'{param}: {value}')
            return super().invoke(ctx)

    return ConfigCommand
