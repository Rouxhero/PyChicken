# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
from app.core.controller.Controller import Controller


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
        from database.models.user import User
        return self.render("index", {"title": "username"})
