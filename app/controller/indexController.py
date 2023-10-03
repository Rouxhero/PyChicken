

from app.controller.core.Controller import Controller
from app.core.mailer import Mailler
from app.models.core.model import ModelFactory
from app.models.user import User

class indexController(Controller):

    def index(self):
        return self.render("index",{"title":"A"})
    
    def about_page(self):
        return self.render("about_page")
    
    def send(self,**post):
        mailler = Mailler()
        user = ModelFactory.create(User,**post)
        mailler.send(post['email'],'Welcome','welcome',{"name":post['username']})

    def regesiter(self,**post):
        # Check username
        # Creer model
        return 