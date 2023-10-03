

import json,os


class Config(dict):

    def __init__(self,path="./.conf"):
        print(os.getcwd())
        self.path = path
        self.config = {}
        self.load()
    
    def load(self):
        with open(self.path, 'r') as f:
            data = json.load(f)
        for key, value in data.items():
            self.__setitem__(key, value)