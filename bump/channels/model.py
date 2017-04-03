from bump import DB as db

class Channel(db.Model):
    __tablename__ = 'channels'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    name = db.Column(db.String(50), unique=True)
    desc = db.Column(db.String(250))
    subscribers = db.relationship('Subscription', backref='channel')

    def __init__(self, name=None, desc=None):
        self.name = name
        self.desc = desc
