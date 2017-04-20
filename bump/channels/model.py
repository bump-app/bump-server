from bump import DB as db
from bump.base_model import Base

class Channel(db.Model, Base):
    __tablename__ = 'channels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(250))
    subscribers = db.relationship('Subscription', backref='channel')
    posts = db.relationship('Post', backref='channel')
