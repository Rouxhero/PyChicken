# -*- coding: utf-8 -*-
# oOoOo Authors oOoOo
#      Rouxhero
#      Alexandre
# -------------------
from datetime import datetime


from app.core.tools import hashP
from app.models.core import Model


class User(Model):

    fields = {
        "email": ("", "required"),
        "firstname": ("", "required"),
        "lastname": ("", "required"),
        "password": ("", "required"),
        "age": (0, "required"),
        "birthdate": (datetime.now().date(), "required"),
    }

    