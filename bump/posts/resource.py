from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from bump import DB as db, oauth2
from bump.posts.schema import PostSchema
from bump.posts.model import Post

class PostList(ResourceList):
        schema = PostSchema
        data_layer = { 'session': db.session,
                       'model': Post }
        decorators = (oauth2.require_oauth('email'),)

class PostDetail(ResourceDetail):
        schema = PostSchema
        data_layer = { 'session': db.session,
                       'model': Post }
        decorators = (oauth2.require_oauth('email'),)

class PostRelationship(ResourceRelationship):
        schema = PostSchema
        data_layer = { 'session': db.session,
                       'model': Post }
