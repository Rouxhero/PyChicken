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
        self.controller = controller
        self.handler = handler
