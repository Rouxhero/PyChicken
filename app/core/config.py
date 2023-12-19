# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
import json, os


class Config(dict):
    """
    PyChicken Config object
    """

    def __init__(self, path="./.conf"):
        """
        Config constructor

        Args:
            path (str, optional): Config path. Defaults to "./.conf".
        """
        self.path = path
        self.config = {}
        self.load()

    def load(self):
        """
        Load config from file, if doesn't existe, create
        """
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
            for key, value in data.items():
                self.__setitem__(key, value)
        except FileNotFoundError:
            print("Config file not found, Creating !")
            with open(self.path, "w+") as f:
                json.dump(default_config, f)


default_config = {
    "database": {"host": "localhost", "user": "root", "password": "", "database": ""},
    "smtp": {"host": "smtp.mail.com", "port": 587, "user": "", "password": ""},
}
