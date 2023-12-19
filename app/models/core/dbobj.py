from collections.abc import MutableMapping
import datetime
import json
from app.core.tools import date_formarter
from app.resources.entry import db


class DbObject(MutableMapping):

    fields: dict = {}

    def __init__(self, kwargs={}):
        self.iFields = self.fields.copy()
        self.changes = dict((k, self.iFields[k][0]) for k in self.fields.keys())
        if kwargs != {}:
            self._create(**kwargs)

    def _create(self, **args) -> None:
        for k in self.fields.keys():
            if k not in args.keys() and self.fields[k][1] == "required":
                raise KeyError(
                    f"[Model][{self.__class__.__name__}][Create Error] {k} is not defined !"
                )
        row = db.insert(self.__class__.__name__, args, hasattr(self, "mId"))
        self.__load_row(self, row)

    def save(self) -> None:
        db.update(self.__class__.__name__, self.changes, self)

    def get(self, **args):
        for k in args.keys():
            if k not in self.keys() and k != "id":
                raise KeyError(
                    f"[Model][{self.__class__.__name__}][Get Error] {k} is not defined !"
                )
        if hasattr(self, "mId"):
            fields = self.fields.copy()
            fields["id"] = ["int", "required"]
        else:
            fields = self.fields.copy()
        row = db.select(self.__class__.__name__, args, fields)
        if row == None:
            return None
        self.__load_row(self, row)
        return self

    def get_all(self, **args):
        for k in args.keys():
            if k not in self.keys() and k != "id":
                raise KeyError(
                    f"[Model][{self.__class__.__name__}][Get Error] {k} is not defined !"
                )
        if hasattr(self, "mId"):
            fields = self.fields.copy()
            fields["id"] = ["int", "required"]
        else:
            fields = self.fields.copy()
        row = db.select(self.__class__.__name__, args, fields, -1)
        if row == None:
            return []
        return [self.__load_row(self.__class__(), r) for r in row]

    def __load_row(self, dest, row):
        if hasattr(dest, "mId"):
            dest.mId = row["id"]
        for k in list(dest.fields.keys()):
            dest = self.append_field(dest, k, row[k])
        return dest

    def append_field(self, dest, k, v):
        if k == None:
            return dest
        elif type(dest.fields[k][0]) == dict:
            dest[k] = json.loads(v)
        elif type(dest.fields[k][0]) == list:
            dest[k] = json.loads(v)
        elif type(dest.fields[k][0]) == int:
            dest[k] = int(v)
        elif type(dest.fields[k][0]) == bool:
            dest[k] = bool(v)
        else:
            dest[k] = v
        return dest

    def delete(self):
        if hasattr(self, "mId"):
            db.delete(self.__class__.__name__, {"id": self.mId})
        else:
            db.delete(self.__class__.__name__, self.iFields)

    def __delitem__(self, key):
        if key not in self.fields:
            raise KeyError(
                f"[Model][{self.__class__.__name__}][Del Error] {key} is not defined !"
            )
        self.iFields[key] = None

    def __setitem__(self, key, value):
        if not key in self.fields:
            raise KeyError(
                f"[Model][{self.__class__.__name__}][Set Error] {key} is not defined !"
            )
        if type(value) != type(self.fields[key][0]) and value != None:
            raise TypeError(
                f"[Model][{self.__class__.__name__}][Set Error] {key} is {type(self.fields[key][0])} not  {type(value)} !"
            )
        if not type(self.iFields[key]) == tuple:
            self.changes[key] = self.iFields[key]
        else:
            self.changes[key] = value
        self.iFields[key] = value

    def __getitem__(self, key):
        if key not in self.fields:
            raise KeyError(
                f"[Model][{self.__class__.__name__}][Get Error] {key} is not defined !"
            )
        return self.iFields[key]

    def __iter__(self):
        return iter(self.iFields)

    def __len__(self):
        return len(self.iFields)
