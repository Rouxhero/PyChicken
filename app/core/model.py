# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
#-------------------
import inspect

class Model:


    fields = []

    def __init__(self) -> None:
       pass


    def create(classtype,*args):
        print(inspect.getmembers((classtype)))
        # for k in classtype.__getattribute__("fields"):
        #     print(k)
        # for k in classtype.fields:
        #     if k not in args:
        #         raise Exception(f"[Model][Create Error] {k} is not defined !")
        # global db
        # db.insert(classtype.__class__.__name__, args)


