# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
from app.controller.core.Controller import Controller


from app.tools.tools import config


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
        # from app.models.user import User
        # from app.models.role import Role
        # from app.models.userrole import UserRole
        # user =User().get_all(username="rouxhero")[0]
        # user["phone"] = 600000001
        # user.save()
        from app.design.core.page import Page, Header, FullScreenSection,Image
        self.page =  Page("index").add_component(
                    "header",
                    Header("header")
                        .add_image(Image("logo", "logo.png"))
                        .add_image(Image("logo", "logo.png"))
                )
        return self.render("index", {"title": "username"})
