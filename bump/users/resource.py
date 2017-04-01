from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from bump import DB as db
from bump.users import schema, model

class UserList(ResourceList):
	schema = schema
	data_layer = {	'session': db.session,
					'model': model}

class UserDetail(ResourceDetail):
	schema = schema
	data_layer = {	'session': db.session,
					'model': model}

class UserRelationship(ResourceRelationship):
	schema = schema
	data_layer = {	'session': db.session,
					'model': model}
