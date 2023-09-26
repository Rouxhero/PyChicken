

class Middleware:

    def __init__(self):
        self.auth = False
        self.appname = "Rendez-Vous"
        


    def auth_u(self, username, password):
        self.auth = True
        return True