
from app.core.tools import env

class Controller:

    def __init__(self):
        pass

    def render(self, name,data={}):
        # Charger le modèle depuis le fichier
        template = env.get_template(name+'.html')
        
        # Rendre le modèle avec les données
        output = template.render(data)
        
        # Retourner la sortie HTML générée
        return output
        