# -*- coding: utf-8 -*-
import datetime

from app.models.core import Model,Fields


class User (Model):

    fields = [
		Fields('username',str,requierd=True),
		# Fields('firstname',str,requierd=True),
		# Fields('lastname',str,requierd=True),
		# Fields('email',str,requierd=True),
		# Fields('birth',datetime.datetime,requierd=True),
		Fields('password',str,requierd=True),
		Fields('phone',int,requierd=True),
		# Fields('email_verified',bool,requierd=True,default=False),
	]
