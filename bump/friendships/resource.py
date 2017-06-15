from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from bump import DB as db
from bump.friendships.schema import FriendshipSchema
from bump.friendships.model import Friendship
from bump.users.model import User

    
class FriendshipList(ResourceList):
    def after_create_object(self, obj, data, **view_kwargs):
        if Friendship.query.filter_by(user_id=obj['friend']).filter_by(friend_id=obj['user']).first() is not None:
            db.session.delete(Friendship.query.filter_by(user_id=obj['user']).
            filter_by(friend_id=obj['friend']).first())
            db.session.commit()

    schema = FriendshipSchema
    data_layer = {'session': db.session,
                  'model': Friendship,
                  'after_create_object': after_create_object}

class FriendshipDetail(ResourceDetail):
    schema = FriendshipSchema
    data_layer = {'session': db.session,
                  'model': Friendship}

class FriendshipRelationship(ResourceRelationship):
    schema = FriendshipSchema
    data_layer = {'session': db.session,
                  'model': Friendship}
