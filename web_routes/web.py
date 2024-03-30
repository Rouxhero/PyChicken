from app.controller.indexController import indexController
from app.core.route import Route


routes = [
    Route("/", "GET", indexController, "index").name("index"),
    Route("/test", "GET", indexController, "test").name("test"),

]
