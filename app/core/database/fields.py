# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------


import datetime


class Fields:

    def __init__(self, name:str, type:type, requierd=False, default=None, unique=False, primary=False, key=False, foreign_table=None, foreign_key=None):
        self.name = name
        self.type = type
        self.requierd = requierd
        self.default = default
        self.unique = unique
        self.primary = primary
        self.foreign_table = foreign_table
        self.foreign_key = foreign_key

    
    def __str__(self):
        sql = f"\t{self.name} {loadType(self.type)}"
        if self.requierd:
            sql += " NOT NULL"
        if self.default is not None:
            sql += f" DEFAULT {self.default}"
        if self.unique:
            sql += " UNIQUE"
        if self.primary:
            sql += " PRIMARY KEY"
        if self.foreign_table is not None and self.foreign_key is not None:
            sql += f" ,\nFOREIGN KEY ({self.name}) REFERENCES {self.foreign_table}({self.foreign_key})"
        return sql 

    



def loadType(type_):
    if type_ == str:
        return "varchar(255)"
    if type_ == int:
        return "int"
    if type_ == float:
        return "float"
    if type_ == bool:
        return "boolean"
    if type_ == datetime.datetime:
        return "datetime"
    return "varchar(255)"
