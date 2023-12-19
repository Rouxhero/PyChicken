# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
from app.controller.core.Controller import Controller
from app.core.tools import config



class indexController(Controller):
    """
    Exemple IndexController
     ** Extent of controller for template engine **
    """

    def index(self, **post) -> str:
        """
        Index method

        Returns:
            str: HTML Page
        """
        
        return self.render("index",{"title":config["app_name"]})
