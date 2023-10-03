# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------

from app.resources.entry import db


class Model:

    pid: int = None
    fields: dict = {}

    def __init__(self) -> None:
        pass

    def update(self, **args) -> None:
        for k in args.keys():
            if k not in self.fields.keys():
                raise Exception(f"[Model][Update Error] {k} is not defined !")
        args["id"] = self.pid
        db.update(self.__class__.__name__, args)


class ModelFactory:
    @staticmethod
    def create(aClass, **args):
        for k in aClass.fields.keys():
            if k not in args.keys():
                raise Exception(f"[Model][Create Error] {k} is not defined !")
        row = db.insert(aClass.__name__, args)
        instance = aClass()
        for k in row:
            instance.fields[k] = row[k]
        return instance
