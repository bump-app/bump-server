from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from bump import DB as db
from bump.comments.schema import CommentSchema
from bump.comments.model import Comment

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
