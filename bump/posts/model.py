from bump import DB as db
from bump.base_model import Base
from bump.posts import constants as POST
from pyembed.core import PyEmbed

class Post(db.Model, Base):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String)
    link_formatted = db.Column(db.String)
    text = db.Column(db.String(POST.TEXT_LENGTH))
    rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))
    comments = db.relationship('Comment', backref='post')

    def __init__(self, **kwargs):
        super(Post, self).__init__(**kwargs)
        try:
            self.link_formatted = PyEmbed().embed(kwargs['link'])
        except:
            pass
