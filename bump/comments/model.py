from bump import DB as db
from bump.comments import constants as COMMENT

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(COMMENT.COMMENT_LENGTH))
    rating = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    post = db.relationship('Post', backref=db.backref('comments'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('comments'))

    def __init__(self, text=None, post_id=None, user_id=None):
        self.text = text
        self.post_id = post_id
        self.user_id = user_id
