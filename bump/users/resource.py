from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from bump import DB as db
from bump.users.schema import UserSchema
from bump.users.model import User

class UserList(ResourceList):
	schema = UserSchema
	data_layer = {	'session': db.session,
					'model': User}

class UserDetail(ResourceDetail):
	schema = UserSchema
	data_layer = {	'session': db.session,
					'model': User}

class UserRelationship(ResourceRelationship):
	schema = UserSchema
	data_layer = {	'session': db.session,
					'model': User}
