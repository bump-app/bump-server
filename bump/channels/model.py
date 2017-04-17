from bump import DB as db

class Channel(db.Model):
    __tablename__ = 'channels'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(250))
    subscribers = db.relationship('Subscription', backref='channel')
    posts = db.relationship('Post', backref='channel')
