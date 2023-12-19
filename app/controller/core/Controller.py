# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
import cherrypy
from app.core.tools import env, config


class Controller:
    """
    Controller class
    """

    def __init__(self):
        self.error = ""
        self.success = ""
        self.warning = ""

    def render(self, name: str, data: dict = None) -> str:
        """
        Render a Jinja template

        Args:
            name (str): template Name
            data (dict, optional): Data to add on the template. Defaults to {}.

        Returns:
            str: _description_
        """
        if data is None:
            data = {}
        if not "context" in data:
            baseURI = "http://"+ config["url"] 
            if config['usePort']:
                    baseURI += ":"+str(config['port'])
            uri = "http://" + config["host"]
            if config['usePort']:
                uri += ":" + str(config["port"]) + "/"
            data["context"] = {
                "basename": baseURI + "/",
                "uri": uri + "/",
                "session": cherrypy.session,
            }
        if "redirect_error" in cherrypy.session.keys():
            data["context"]["error"] = cherrypy.session["redirect_error"]
            cherrypy.session["redirect_error"] = ""
        if "redirect_success" in cherrypy.session.keys():
            data["context"]["success"] = cherrypy.session["redirect_success"]
            cherrypy.session["redirect_success"] = ""
        if "redirect_warning" in cherrypy.session.keys():
            data["context"]["warning"] = cherrypy.session["redirect_warning"]
            cherrypy.session["redirect_warning"] = ""
        if self.error != "":
            data["context"]["error"] = self.error
            self.error = ""
        if self.success != "":
            data["context"]["success"] = self.success
            self.success = ""
        if self.warning != "":
            data["context"]["warning"] = self.warning
            self.warning = ""

        template = env.get_template(name + ".html")
        output = template.render(data)
        return output

    def redirect(self, path: str) -> str:
        """
        Redirect to a path

        Args:
            path (str): Path to redirect

        Returns:
            str: _description_
        """
        if self.error != "":
            cherrypy.session["redirect_error"] = self.error
        if self.success != "":
            cherrypy.session["redirect_success"] = self.success
        if self.warning != "":
            cherrypy.session["redirect_warning"] = self.warning
        raise cherrypy.HTTPRedirect(path)
