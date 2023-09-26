# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
#-------------------


class Middleware:

    def __init__(self,name:str="CherryPy"):
        self.auth = False
        self.appname = name
        


    def auth_u(self, username, password):
        self.auth = True
        return True