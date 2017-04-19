from bump import DB as db
from bump.posts import constants as POST

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    link = db.Column(db.String)
    text = db.Column(db.String(POST.TEXT_LENGTH))
    rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))
    comments = db.relationship('Comment', backref='post')
