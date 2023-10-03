# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
from app.core.tools import env


class Controller:
    """
    Controller class
    """    
    
    def __init__(self):
        pass

    def render(self, name:str, data:dict={})->str:
        """
        Render a Jinja template

        Args:
            name (str): template Name
            data (dict, optional): Data to add on the template. Defaults to {}.

        Returns:
            str: _description_
        """            
        template = env.get_template(name + ".html")
        output = template.render(data)
        return output
