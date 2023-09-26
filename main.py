
# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
#-------------------

import cherrypy
from app.core import Middleware,Template,Database,Model
import os

from app.models.user import User


db = Database(
    host='localhost',
    user='root',
    password='',
    database='db'
)

class WebSite(object):

    def __init__(self) -> None:
        global db
        self.db = db
        self.middlware = Middleware()
        self.template = Template(self.middlware,"views")

    @cherrypy.expose
    def index(self):
        Model.create(User,{
            "username":"test",
            "password":"test",
            "email":"test@test.com"
        })
        return self.template.render("index",{"var":"coucou","name":"email"})
    

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(WebSite(), '/', conf)
