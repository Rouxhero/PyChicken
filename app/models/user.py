# -*- coding: utf-8 -*-
from datetime import datetime

from app.models.core import Model


class User (Model):

    fields = {
		'name':('','requierd'),
		'email':('','requierd'),
		'birth':(datetime.datetime.now(),'requierd'),
		'phone':(1,'requierd'),
    }
