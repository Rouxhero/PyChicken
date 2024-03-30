# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
import cherrypy
from app.tools.tools import env, config



code = ["error", "success", "warning"]


class Controller:
    """
    Controller class
    """

    def __init__(self):
        self.error = ""
        self.success = ""
        self.warning = ""
        self.page = None

    def render(self, name: str, data: dict = None) -> str:
        """
        Render a Jinja template

        Args:
            name (str): template Name
            data (dict, optional): Data to add on the template. Defaults to {}.

        Returns:
            str: _description_
        """
        from app.design import front
        if data is None:
            data = {}
        if not "context" in data:
            baseURI = "http://" + config["url"]
            if config["usePort"]:
                baseURI += ":" + str(config["port"])
            uri = "http://" + config["host"]
            if config["usePort"]:
                uri += ":" + str(config["port"]) + "/"
            data["context"] = {
                "basename": baseURI + "/",
                "uri": uri + "/",
                "session": cherrypy.session,
            }
            if self.page is not None:
                front.add_component("page", self.page)
            data["front"] = front
            data["routes"] = config["routes"]

        for c in code:
            rc = "redirect_"+c
            if rc in cherrypy.session.keys():
                data["context"][c] = cherrypy.session[rc]
                cherrypy.session[rc] = ""
        for c in code:
            if self.__getattribute__(c) != "":
                data["context"][c] = self.__getattribute__(c)
                self.__setattr__(c, "")

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
