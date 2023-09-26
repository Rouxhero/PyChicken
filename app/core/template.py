# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
#-------------------

import io,re

from app.core import Middleware


class Template:

    def __init__(self,middleware:Middleware,root:str="")-> None:
        """
        Init template

        Args:
            middleware (Middleware): Middleware instance
            root (str, optional): Root dicroty of template directory. Defaults to "".
        """
        self.root = root
        self.middleware = middleware
    
    def render(self, viewName:str,args:dict={})->str:
        """
        render the view, with given args

        Args:
            viewName (str): view name
            args (list, optional): args list. Defaults to [].

        Returns:
            str: _description_
        """
        page = io.open(f"{self.root}/{viewName}.html","r",encoding='utf8').read()
        page = self.__render_componnent(page)
        page = page.replace("{{appname}}",self.middleware.appname)
        for key,val in args.items():
            page = page.replace("{{"+key+"}}",val)
        return page

    def __render_componnent(self,page:str)->str:
        """
        render all componnent in page

        Args:
            page (str): the current page

        Returns:
            str: the page with componnent
        """        
        allCompo = re.findall(r"#include\(\"[\w\.]+\"\)", page)
        print(allCompo)
        if allCompo != []:
            for compo in allCompo:
                compon = re.search(r"#include\(\"(?P<compo>[\w\.]+)\"\)",compo).groups()[0]
                page = page.replace(f'#include("{compon}")',self.render(compon.replace(".","/")))
        return page