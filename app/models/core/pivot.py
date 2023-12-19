from app.models.core.dbobj import DbObject


class Pivot(DbObject):
    def __init__(self, kwargs={}):
        super(Pivot, self).__init__(kwargs)
