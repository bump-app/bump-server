from bump import DB as db
from bump.posts import constants as POST

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    title = db.Column(db.String(POST.TITLE_LENGTH))
    text = db.Column(db.String(POST.POST_LENGTH))
    rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))
    comments = db.relationship('Comment', backref='post')
