from app.core.routeloader import RouteLoader
# Import here your routes
from app.route.web import routes as web_routes
from app.route.auth import routes as auth_routes


# Add your routes here
routes = web_routes
# routes += auth_routes

