# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------

import json
from app.models.core.dbobj import DbObject


class Model(DbObject):

    mId: int = 0

    def __init__(self, kwargs={}):
        super(Model, self).__init__(kwargs)

    @property
    def id(self):
        return self.mId

    @id.setter
    def id(self, value):
        self.mId = value
