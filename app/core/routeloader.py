


from typing import MutableMapping


class RouteLoader(MutableMapping):
    
    def __init__(self,routes):
        self.routes = routes
    
    def __getitem__(self, key):
        for route in self.routes:
            if route.name_ == key:
                return route
        raise KeyError(f"Route {key} not found ")

    def __setitem__(self, key, value):
        for route in self.routes:
            if route.name_ == key:
                raise KeyError("Route already exists")
        self.routes.append(value)
    
    def __delitem__(self, key):
        for route in self.routes:
            if route.name_ == key:
                self.routes.remove(route)
                return
        raise KeyError("Route not found")

    def __iter__(self):
        return iter(self.routes)

    def __len__(self):
        return len(self.routes)
    
    def get(self, key,default=None):
        try:
            return self[key]
        except KeyError:
            return default

        