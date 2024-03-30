# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------


class Route:
    def __init__(self, path: str, method: str, controller, handler: str):
        """
        Route constructor.

        Args:
            path (str): url of route
            method (str): Access type
            controller (class): The controller class to call 
            handler(str): The controller method who handle the request 
        """
        self.path = path
        self.method = method
        self.name_ = ""
        self.controller = controller
        self.handler = handler
    
    def name(self, name: str):
        """
        Set the name of the route

        Args:
            name (str): Name of the route
        """
        self.name_ = name
        return self
    def __str__(self):
        return f"{self.path}"
