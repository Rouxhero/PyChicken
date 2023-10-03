import sys
from app.core.databse import Database
from app.core.tools import log,config

try:
    log(f"[green][INFO] Start Database")
    print(config)
    db = Database(**config["database"])
    log(f"[green][INFO][DataBase] Database connected ! ")
except Exception as e:
    log(f"[red][ERROR][DataBase] Error during database creation : {e}")
    sys.exit(1)


# smtp = STMP()
