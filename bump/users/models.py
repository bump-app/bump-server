from bump import DB
from bump.users import constants as USER

class User(db.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(50), unique=True)
    email = DB.Column(DB.String(120), unique=True)
    password = DB.Column(DB.String(120))
    role = db.Column(DB.SmallInteger, default=USER.USER)
    status = db.Column(DB.SmallInteger, default=USER.NEW)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def getStatus(self):
        return USER.STATUS[self.status]

    def getRole(self):
        return USER.ROLE[self.role]

    def __repr__(self):
        return '<User %r>' % (self.name)
