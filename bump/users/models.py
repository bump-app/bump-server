from bump import DB
from bump.users import constants as USER

class User(db.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
