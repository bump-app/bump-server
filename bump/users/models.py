"""User models

This module contains SQLAlchemy model classes for the users package.

"""

from bump import DB as db
from bump.users import constants as USER

# FIXME
#from bump.posts.models import Post 

class User(db.Model):
    """User model class for SQLAlchemy."""

    __tablename__ = 'users_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    role = db.Column(db.SmallInteger, default=USER.USER)
    status = db.Column(db.SmallInteger, default=USER.NEW)
    posts = db.relationship('Post', backref='user', lazy='dynamic')

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def get_status(self):
        return USER.STATUS[self.status]

    def get_role(self):
        return USER.ROLE[self.role]

    def __repr__(self):
        return '<User {name}>'.format(name=self.name)
