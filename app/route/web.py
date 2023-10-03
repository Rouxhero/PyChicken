
from collections import namedtuple

from app.controller.indexController import indexController
from app.core.route import Route


web_routes = [
    Route('/', 'GET', indexController,'index'),
    Route('/about', 'GET', indexController,'about_page'),
    Route('/send','POST',indexController,'send')
]   



