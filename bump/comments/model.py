from bump import DB as db
from bump.base_model import Base
from bump.comments import constants as COMMENT

class Comment(db.Model, Base):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(COMMENT.COMMENT_LENGTH))
    rating = db.Column(db.Integer)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
