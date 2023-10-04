# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
import cherrypy
import os

from app.core.tools import log
from app.core import WebApp

"""
   _____ _                          _____         ______                     __          __        _    
  / ____| |                        |  __ \       |  ____|                    \ \        / /       | |   
 | |    | |__   ___ _ __ _ __ _   _| |__) |   _  | |__ _ __ __ _ _ __ ___   __\ \  /\  / /__  _ __| | __
 | |    | '_ \ / _ \ '__| '__| | | |  ___/ | | | |  __| '__/ _` | '_ ` _ \ / _ \ \/  \/ / _ \| '__| |/ /
 | |____| | | |  __/ |  | |  | |_| | |   | |_| | | |  | | | (_| | | | | | |  __/\  /\  / (_) | |  |   < 
  \_____|_| |_|\___|_|  |_|   \__, |_|    \__, | |_|  |_|  \__,_|_| |_| |_|\___| \/  \/ \___/|_|  |_|\_\ 
                               __/ |       __/ |                                                        
                              |___/       |___/                                                         

                              
    Welcome on CherryPy FrameWork
"""

if __name__ == "__main__":
    conf = {
        "/": {
            "tools.sessions.on": True,
            "request.dispatch": WebApp().router,
            "tools.staticdir.root": os.path.abspath(os.getcwd()),
        },
        "/static": {"tools.staticdir.on": True, "tools.staticdir.dir": "./public"},
    }
    cherrypy.config.update({'tools.sessions.on': True,
                        'tools.sessions.storage_type': "File",
                        'tools.sessions.storage_path': 'cache/sessions',
                        'tools.sessions.timeout': 10
               })


    cherrypy.quickstart(None, "/", conf)
