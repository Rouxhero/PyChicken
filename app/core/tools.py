# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
from rich.console import Console
from rich.logging import RichHandler
from jinja2 import Environment, FileSystemLoader
import cherrypy
from app.core.config import Config

# Logs
console = Console()
log = lambda x: console.log(x)
ch = RichHandler(console=console, markup=True)
cherrypy.log.error_log.addHandler(ch)
# Templates
env = Environment(loader=FileSystemLoader("./app/resources/views"))
mail_env = Environment(loader=FileSystemLoader("./app/resources/mails"))
# Configuration
config = Config()
