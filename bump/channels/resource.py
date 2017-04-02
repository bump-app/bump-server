from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from bump import DB as db
from bump.channels.schema import ChannelSchema
from bump.channels.model import Channel

class ChannelList(ResourceList):
	schema = ChannelSchema
	data_layer = {	'session': db.session,
					'model': Channel}

class ChannelDetail(ResourceDetail):
	schema = ChannelSchema
	data_layer = {	'session': db.session,
					'model': Channel}

class ChannelRelationship(ResourceRelationship):
	schema = ChannelSchema
	data_layer = {	'session': db.session,
					'model': Channel}
