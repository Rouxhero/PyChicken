

import cherrypy
from app import Middleware,Template
import io,os

class WebSite(object):

    def __init__(self) -> None:
        self.middlware = Middleware()
        self.template = Template(self.middlware,"views")

    @cherrypy.expose
    def index(self):
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
