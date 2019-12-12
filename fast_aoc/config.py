""" Module for handling package configurations
"""
import json
import os


class Config:
    """ Class defining package configuration
    """
    CONFIG_FOLDER = os.path.join(os.path.expanduser('~'), '.config', 'aocd')

    DEFAULT_CONFIG = {
        'token': None,
        'folder': None
    }

    def __init__(self, reset=False, raise_undefined=False, **kwargs):
        """
        :param reset: If True it will set default values instead of loading existing ones
        :type reset: bool
        :param raise_undefined: Raises an error if some of required parameters are undefined
        :type raise_undefined: bool
        :param kwargs: Any parameter defined in DEFAULT_DICT
        """
        if reset:
            self._config = self.DEFAULT_CONFIG.copy()
        else:
            self._config = self.load()

        for param, value in kwargs.items():
            if param not in self._config:
                raise ValueError(f"Parameter '{param}' cannot be added to config")

            if value is not None:
                self._config[param] = value

        if raise_undefined and self.token is None:
            raise RuntimeError('You have to configure at least your token')

    def __getattr__(self, name):
        """ This is called only if the class doesn't have the attribute itself
        """
        if name in self._config:
            return self._config[name]

        return super().__getattribute__()

    def __str__(self):
        """ Content of Config in json schema
        """
        return json.dumps(self._config, indent=2)

    def save(self):
        """ Saves config to local storage
        """
        with open(self.get_config_path(create=True), 'w') as cfg_file:
            json.dump(self._config, cfg_file, indent=2)

        if self.token:
            token_path = os.path.join(self.CONFIG_FOLDER, 'token')
            with open(token_path, 'w') as token_file:
                token_file.write(self.token)

    @classmethod
    def load(cls):
        """ Loads config from local storage
        """
        config_path = cls.get_config_path()
        if not os.path.exists(config_path):
            return cls.DEFAULT_CONFIG.copy()

        with open(config_path, 'r') as cfg_file:
            config = json.load(cfg_file)

        for param, value in cls.DEFAULT_CONFIG.items():
            if param not in config:
                config[param] = value

        return config

    @classmethod
    def get_params(cls):
        """ Provides a list of config parameters
        """
        return [param for param in cls.DEFAULT_CONFIG]

    @classmethod
    def get_config_path(cls, create=False):
        """ Provides a file path to the config file
        """
        if create and not os.path.exists(cls.CONFIG_FOLDER):
            os.makedirs(cls.CONFIG_FOLDER)

        return os.path.join(cls.CONFIG_FOLDER, 'fast_aoc_config.json')
