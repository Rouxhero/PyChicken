from app.controller.ajaxController import AjaxController
from app.controller.indexController import indexController
from app.core.route import Route


routes = [
    Route("/", "GET", indexController, "index"),
]
