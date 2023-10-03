# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
import cherrypy
from app.resources.entry import db
from app.route import routes


class WebApp(object):

    appname = "CherryPy FrameWork"

    def __init__(self) -> None:
        self.db = db
        self.router = cherrypy.dispatch.RoutesDispatcher()
        for route in routes:
            self.router.connect(
                name=route.path,
                route=route.path,
                controller=route.controller,
                action=route.handler,
                conditions={"method": [route.method]},
            )

    def default(self, *args, **kwargs):
        # Récupérez le contrôleur et la méthode à appeler à partir des arguments
        controller = kwargs["controller"]
        action = kwargs["action"]

        # Appelez la méthode du contrôleur
        return getattr(controller, action)()
