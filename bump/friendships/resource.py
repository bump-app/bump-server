from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from bump import DB as db
from bump.friendships.schema import FriendshipSchema
from bump.friendships.model import Friendship

class FriendshipList(ResourceList):
    schema = FriendshipSchema
    data_layer = {'session': db.session,
                  'model': Friendship}

class FriendshipDetail(ResourceDetail):
    schema = FriendshipSchema
    data_layer = {'session': db.session,
                  'model': Friendship}

class FriendshipRelationship(ResourceRelationship):
    schema = FriendshipSchema
    data_layer = {'session': db.session,
                  'model': Friendship}
