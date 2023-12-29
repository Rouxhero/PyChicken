import cherrypy


def auth(func):
    def wrapper(*args, **kwargs):
        if not cherrypy.session.get("id_user"):
            raise cherrypy.HTTPRedirect("/auth/login")
        return func(*args, **kwargs)

    return wrapper
