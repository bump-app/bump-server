from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from bump import DB as db
from bump.posts.schema import PostSchema
from bump.posts.model import Post
from bump.users.model import User

class PostList(ResourceList):
	schema = PostSchema
	data_layer = {	'session': db.session,
					'model': Post}

class PostDetail(ResourceDetail):
	schema = PostSchema
	data_layer = {	'session': db.session,
					'model': Post}

class PostRelationship(ResourceRelationship):
	schema = PostSchema
	data_layer = {	'session': db.session,
					'model': Post}
