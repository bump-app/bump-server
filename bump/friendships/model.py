from bump import DB as db
from bump.base_model import Base

class Friendship(db.Model, Base):
    __tablename__ = 'friendships'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    confirmed = db.Column(db.Boolean, default=False)
    __table_args__ = (db.UniqueConstraint('user_id', 'friend_id',
        name='_user_friend_uc'),
        )
