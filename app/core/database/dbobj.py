from collections.abc import MutableMapping
import datetime
import json



global db

class DbObject(MutableMapping):

    fields: dict = []
    
    def __init__(self, kwargs={}):
        self.iFields = dict((k.name, (k.type,k.requierd)) for k in self.fields)
        self.changes = dict((k.name, k.type) for k in self.fields)
        if kwargs != {}:
            self._create(**kwargs)

    def _create(self, **args) -> None:
        
        for k in self.fields:
            if k.name not in args.keys() and k.requierd:
                raise KeyError(
                    f"[Model][{self.__class__.__name__}][Create Error] {k.name} is not defined !"
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
        fields = dict((k.name,[k.type,k.requierd]) for k in self.fields)
        if hasattr(self, "mId"):
            fields["id"] = ["int", "required"]

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
        fields = dict((k.name,[k.type,k.requierd]) for k in self.fields)
        if hasattr(self, "mId"):
            fields["id"] = ["int", "required"]
        row = db.select(self.__class__.__name__, args, fields, -1)
        if row == None:
            return []
        return [self.__load_row(self.__class__(), r) for r in row]

    def __load_row(self, dest, row):
        if hasattr(dest, "mId"):
            dest.mId = row["id"]
        for k in dest.fields:
            dest = self.append_field(dest, k, row[k.name])
        return dest

    def append_field(self, dest, k, v):
        if k == None:
            return dest
        elif k.type == dict:
            dest[k.name] = json.loads(v)
        elif k.type == list:
            dest[k.name] = json.loads(v)
        elif k.type == int:
            dest[k.name] = int(v)
        elif k.type == bool:
            dest[k.name] = bool(v)
        else:
            dest[k.name] = v
        return dest

    def delete(self):
        if hasattr(self, "mId"):
            db.delete(self.__class__.__name__, {"id": self.mId})
        else:
            db.delete(self.__class__.__name__, self.iFields)

    def __delitem__(self, key):
        if not any(key == k.name for k in self.fields):
            raise KeyError(
                f"[Model][{self.__class__.__name__}][Del Error] {key} is not defined !"
            )
        self.iFields[key] = None

    def __setitem__(self, key, value):
        if not any(key == k.name for k in self.fields):
            raise KeyError(
                f"[Model][{self.__class__.__name__}][Set Error] {key} is not defined !"
            )
        f = [k for k in self.fields if k.name == key][0]
        if type(value) != f.type and value != None:
            raise TypeError(
                f"[Model][{self.__class__.__name__}][Set Error] {key} is {f.type} not  {type(value)} !"
            )
        if not type(self.iFields[key]) == tuple:
            self.changes[key] = self.iFields[key]
        else:
            self.changes[key] = value
        self.iFields[key] = value

    def __getitem__(self, key):
        if not any(key == k.name for k in self.fields):
            raise KeyError(
                f"[Model][{self.__class__.__name__}][Get Error] {key} is not defined !"
            )
        return self.iFields[key]

    def __iter__(self):
        return iter(self.iFields)

    def __len__(self):
        return len(self.iFields)
