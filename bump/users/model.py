from bump import DB as db
from bump.users import constants as USER

friends = db.Table('friends',   db.Column('user_id', db.Integer, db.ForeignKey('users.id'), index=True),
                                db.Column('friend_id', db.Integer, db.ForeignKey('users.id')))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    _role = db.Column(db.SmallInteger, default=USER.USER)
    status = db.Column(db.SmallInteger, default=USER.NEW)
    # clients = db.relationship('Client', backref='user')
    # grants = db.relationship('Grant', backref='user')
    # tokens = db.relationship('Token', backref='user')
    subscriptions = db.relationship('Subscription', backref='user')
    posts = db.relationship('Post', backref='user')
    comments = db.relationship('Comment', backref='user')
    friends = db.relationship(  'User',
                                secondary=friends,
                                primaryjoin=(id == friends.c.user_id),
                                secondaryjoin=(id == friends.c.friend_id))

    def get_status(self):
        return USER.STATUS[self.status]

    def get_role(self):
        return USER.ROLE[self._role]

    def check_password(self, password):
        return self.password == password

    def __repr__(self):
        return '<User {name}>'.format(name=self.name)
