import yaml
from click import Command


def CommandWithConfig(config_param='config', config_default='config.yml'):
    class ConfigCommand(Command):
        """
        Click Command that reads values from a config file
        """

        def invoke(self, ctx):
            config_file = ctx.params[config_param]
            if config_file is not None:
                with open(config_file) as f:
                    config_data = yaml.safe_load(f)
                    for param, value in ctx.params.items():
                        if value is None and param in config_data:
                            ctx.params[param] = config_data[param]

            return super(ConfigCommand, self).invoke(ctx)

    return ConfigCommand


def get_config():
    pass
