# -*- coding: utf-8 -*-
import datetime

from app.core.database import Model,Fields


class User (Model):

    fields = [
		Fields('username',str,requierd=True),
		Fields('password',str,requierd=True),
		Fields('email',str,requierd=True),
	]
