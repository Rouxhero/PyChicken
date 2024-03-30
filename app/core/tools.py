# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
import datetime
from rich.console import Console
from rich.logging import RichHandler
from jinja2 import Environment, FileSystemLoader
import cherrypy
from app.core.config import Config
import hashlib


# Logs
console = Console()
log = lambda x: console.log(x)
ch = RichHandler(console=console, markup=True)
cherrypy.log.error_log.addHandler(ch)
# Templates
env = Environment(loader=FileSystemLoader("./resources/views"))
mail_env = Environment(loader=FileSystemLoader("./resources/mails"))
# Configuration
config = Config()
from app.core.route_loader import routes_loader
config["routes"] =  routes_loader

def hashP(password):
    return hashlib.sha256(password.encode()).hexdigest()

def date_formarter(date: str) -> str:
    return datetime.datetime.strptime(date, "%d/%m/%Y, %H:%M PM").strftime(
        "%Y:%m:%d %H:%M:00"
    )