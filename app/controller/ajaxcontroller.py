# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
# Generated with python tool.py new:Controller ajaxcontroller
from app.controller.core.Controller import Controller
from app.tools.tools import config


class AjaxController(Controller):
    
		def index(self ) -> str:
			return self.render('index')

		def save(self, age, name, email) -> str:
			return self.render('index')

		def create(self, **param) -> str:
			return self.render('index')

