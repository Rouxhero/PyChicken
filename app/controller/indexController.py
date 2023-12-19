# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------

import cherrypy
from faker import Faker
from app.controller.core.Controller import Controller



class indexController(Controller):
    """
    Exemple IndexController
     ** Extent of controller for template engine **
    """    
    def index(self,**post)->str:
        """
        Index method

        Returns:
            str: HTML Page
        """
        print(post)
        if  not 'username' in cherrypy.session:
            cherrypy.session['username'] = Faker().user_name()
        # raise cherrypy.HTTPError(404)
        return self.render("index", {"title": cherrypy.session['username']})
