from bump import DB as db
from bump.base_model import Base

class Subscription(db.Model, Base):
    __tablename__ = 'subscriptions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))
    __table_args__ = (db.UniqueConstraint('user_id', 'channel_id',
        name='_user_channel_uc'),
        )
