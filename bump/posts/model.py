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
    user = db.relationship('User', backref=db.backref('posts'))
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))
    channel = db.relationship('Channel', backref=db.backref('posts'))

    def __init__(self, title=None, text=None, user_id=None):
        self.title = title
        self.text = text
        self.user_id = user_id

    def get_rating(self):
        return self.rating

    def get_user_id(self):
        return self.user_id

    def __repr__(self):
        return '<Post {title} made by {user_id}>'.format(title=self.title,
                                                         user_id=self.user_id)
