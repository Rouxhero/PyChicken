# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
import sys
from app.core.database import Database
from app.core.tools import log, config

db = None
try:
    log(f"[green][INFO] Start Database")
    db = Database(**config["database"])
    log(f"[green][INFO][DataBase] Database connected ! ")
except Exception as e:
    log(f"[red]{e}\n[ERROR][DataBase] No database connected")
