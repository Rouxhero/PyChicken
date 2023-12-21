import argparse
from collections import namedtuple
import datetime
from rich import print as rprint



# Créez le parser principal
parser = argparse.ArgumentParser(description='Outil Python pour assister le développement web')
subparsers = parser.add_subparsers(title='new', dest='make_command', help='Permet de créer différents éléments')

# Fonction pour valider le format du nom (vous pouvez ajuster selon vos besoins)
def validate_name(name):
    if not name.isidentifier():
        raise argparse.ArgumentTypeError(f'Le nom "{name}" n\'est pas valide.')
    return name

# Sous-commande pour 'Controller'
controller_parser = subparsers.add_parser('new:Controller', help='Créer un contrôleur')
controller_parser.add_argument('-c', '--console', action='store_true', help='Option pour la console')
controller_parser.add_argument('-e', '--empty', action='store_true', help='Option pour créer un objet vide(default)')
controller_parser.add_argument('name', type=validate_name, help='Nom de l\'objet à créer')

# Sous-commande pour 'Model'
model_parser = subparsers.add_parser('new:Model', help='Créer un modèle')
model_parser.add_argument('-c', '--console', action='store_true', help='Option pour la console')
model_parser.add_argument('-e', '--empty', action='store_true', help='Option pour créer un objet vide(default)')
model_parser.add_argument('name', type=validate_name, help='Nom de l\'objet à créer')

# Sous-commande pour 'Pivot'
pivot_parser = subparsers.add_parser('new:Pivot', help='Créer un pivot')
pivot_parser.add_argument('-c', '--console', action='store_true', help='Option pour la console')
pivot_parser.add_argument('-e', '--empty', action='store_true', help='Option pour créer un objet vide(default)')
pivot_parser.add_argument('name', type=validate_name, help='Nom de l\'objet à créer')

# Sous-commande pour 'Route'
route_parser = subparsers.add_parser('new:Route', help='Créer une route')
route_parser.add_argument('-c', '--console', action='store_true', help='Option pour la console')
route_parser.add_argument('-e', '--empty', action='store_true', help='Option pour créer un objet vide(default)')
route_parser.add_argument('name', type=validate_name, help='Nom de l\'objet à crée ')

Controller = namedtuple('Controller', ['name', 'methodes'])
Method = namedtuple('Method', ['name', 'params'])
def create_controller(console: bool, empty: bool, name: str):
    rprint(f'Création du contrôleur [bold][green]{name}[/green][/bold]')
    name = name[0].upper()+name[1:]
    controller = Controller(name, [])
    if console:
        rprint("[blue]Configuration du controleur[/blue]")
        val = ""
        while val != "q":
            val = input("Ajouter le nom d'un méthode (q pour terminer): ")
            if val != "q":
                value = Method(val, [])
                rprint("[blue]\tAjouter les paramètres de la méthode[/blue]",end="")
                res = input("([Y]es/[N]o): ")
                if res == "Y":
                    fix = input("\tNombre de paramètres fixe ([Y]es/[N]o): ")
                    if fix == "Y":
                        val_ = ""
                        while val_ != "q":
                            val_ = input("\t\tAjouter le nom d'un paramètre (q pour terminer): ")
                            if val_ != "q":
                                value.params.append(val_)
                    else:
                        value.params.append("**param")
                   
                
                controller.methodes.append(value)
        rprint(f"Resumé du controleur:\n[bold][green]{name}[/green][/bold]:")
        for methode in controller.methodes:
            rprint(f"\t{methode.name}(",end="")
            rprint(", ".join(methode.params),end="")
            rprint(")")
    create_controller_file(controller)
    rprint(f"Le controleur [bold][green]{name}[/green][/bold] a été créé avec succès")

def create_controller_file(controller:Controller):
    args_ = lambda m :','+ ", ".join([f"{param}" for param in m.params])
    method = "\n\n".join([f"\t\tdef {methode.name}(self {args_(methode)}) -> str:\n\t\t\treturn self.render('index')" for methode in controller.methodes])
    with open("app/controller/"+controller.name.lower()+".py","w") as f:
        f.write(f"""# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
# Generated with python tool.py new:Controller {controller.name.lower()}
from app.controller.core.Controller import Controller

class {controller.name}(Controller):
    
{method}

""")


Model = namedtuple("Model",["name","attr"])
Attribute = namedtuple("Attribute",["name","type_","requierd"])
def create_model(console: bool, empty: bool, name: str):
    model = Model(name,[])
    rprint(f'Création du modèle [bold][green]{name}[/green][/bold]')
    name = name[0].upper()+name[1:]
    if console:
        rprint("[blue]Configuration du modèle[/blue]")
        val = ""
        while val != "q":
            val = input("Ajouter le nom d'un attribut (q pour terminer): ")
            if val != "q":
                rprint("[blue]\tAjouter le type de l'attribut[/blue]")
                type_ = parse_type(input("\t\tType: "))
                while type_ == False:
                    rprint("[red]\t\tType invalide[/red]")
                    type_ = parse_type(input("\t\tType: "))
                rprint("[blue]\tAjouter si l'attribut est obligatoire[/blue]")
                requierd = input("\t\tObligatoire ([Y]es/[N]o): ") != "N" # Default True
                model.attr.append(Attribute(val,type_,requierd))
        rprint(f"Resumé du modèle:\n[bold][green]{name}[/green][/bold]:")
        for attr in model.attr:
            rprint(f"\t{attr.name} ({type(attr.type_)})")
    create_model_file(model,name)
    rprint(f"Le modèle [bold][green]{name}[/green][/bold] a été créé avec succès")

def create_model_file(model:Model,name:str):
    r = lambda x : "'requierd'" if x.requierd else'""'
    attr = ",\n".join([f"\t\t'{attr.name}':({attr.type_},{r(attr)})" for attr in model.attr])
    with open("app/models/"+name.lower()+".py","w") as f:
        f.write("""# -*- coding: utf-8 -*-
from datetime import datetime

from app.models.core import Model


class """+model.name+"""(Model):

    fields = {
"""+attr+""",
    }
""")
        
Pivot = namedtuple("Pivot",["name","attr"])
def create_pivot(console: bool, empty: bool, name: str):
    rprint(f'Création du pivot [bold][green]{name}[/green][/bold]')
    name = name[0].upper()+name[1:]
    pivot = Pivot(name,[])
    if console:
        rprint("[blue]Configuration du pivot[/blue]")
        val = ""
        while val != "q":
            val = input("Ajouter le nom d'un attribut (q pour terminer): ")
            if val != "q":
                rprint("[blue]\tAjouter le type de l'attribut[/blue]")
                type_ = parse_type(input("\t\tType: "))
                while type_ == False:
                    rprint("[red]\t\tType invalide[/red]")
                    type_ = parse_type(input("\t\tType: "))
                rprint("[blue]\tAjouter si l'attribut est obligatoire[/blue]")
                requierd = input("\t\tObligatoire ([Y]es/[N]o): ") != "N" # Default True
                pivot.attr.append(Attribute(val,type_,requierd))
        rprint(f"Resumé du modèle:\n[bold][green]{name}[/green][/bold]:")
        for attr in pivot.attr:
            rprint(f"\t{attr.name} ({type(attr.type_)})")
    create_pivot_file(pivot,name)
    rprint(f"Le pivot [bold][green]{name}[/green][/bold] a été créé avec succès")

def create_pivot_file(pivot:Pivot,name:str):
    r = lambda x : "'requierd'" if x.requierd else'""'
    attr = ",\n".join([f"\t\t'{attr.name}':({attr.type_},{r(attr)})" for attr in pivot.attr])
    with open("app/models/"+name.lower()+".py","w") as f:
        f.write("""# -*- coding: utf-8 -*-
from datetime import datetime

from app.models.core import Pivot


class """+pivot.name+"""(Pivot):

    fields = {
"""+attr+""",
    }
""")

def parse_type(input_:str):
    if input_ == "int":
        return 1
    if input_ == "date":
        return "datetime.datetime.now()"
    if input_ == "str":
        return "''"
    if input_ == "float":
        return float(1)
    if input_ == "bool":
        return True
    return False

if __name__ == '__main__':
    args = parser.parse_args()

    # Traitez les arguments en fonction de la sous-commande
    if args.make_command:
        new = args.make_command.split(':')[1]
        console_option = getattr(args, 'console', False)
        empty_option = getattr(args, 'empty', False)
        object_name = args.name

        match new:
            case 'Controller':
                create_controller(console_option, empty_option, object_name)
            case 'Model':
                create_model(console_option, empty_option, object_name)
            case 'Pivot':
                create_pivot(console_option, empty_option, object_name)
            case 'Route':
                print(f'Création d\'une route avec -c={console_option}, -e={empty_option} et le nom "{object_name}"')
    else:
        print('Aucune sous-commande spécifiée')





