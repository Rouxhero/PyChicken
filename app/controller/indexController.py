# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------

from app.controller.core.Controller import Controller


class indexController(Controller):
    """
    Exemple IndexController
     ** Extent of controller for template engine **
    """    
    def index(self)->str:
        """
        Index method

        Returns:
            str: HTML Page
        """
        return self.render("index", {"title": "A"})
