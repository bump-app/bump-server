from bump import DB as db
from bump.users import constants as USER

#roles_users = db.Table('roles_users',
        #db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        #db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

#class Role(db.Model):
    #id = db.Column(db.Integer(), primary_key=True)
    #name = db.Column(db.String(80), unique=True)
    #description = db.Column(db.String(255))

class User(db.Model):
    __tablename__ = 'users_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    role = db.Column(db.SmallInteger, default=USER.USER)
    #roles = db.relationship('Role', secondary=roles_users,
                            #backref=db.backref('users', lazy='dynamic')) 
    status = db.Column(db.SmallInteger, default=USER.NEW)

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

