from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from bump import DB as db
from bump.comments.schema import CommentSchema
from bump.comments.model import Comment
from bump.posts.model import Post
from bump.users.model import User

class CommentList(ResourceList):
	schema = CommentSchema
	data_layer = {	'session': db.session,
					'model': Comment}

class CommentDetail(ResourceDetail):
	schema = CommentSchema
	data_layer = {	'session': db.session,
					'model': Comment}

class CommentRelationship(ResourceRelationship):
	schema = CommentSchema
	data_layer = {	'session': db.session,
					'model': Comment}
