from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from bump import DB as db
from bump.subscriptions.schema import SubscriptionSchema
from bump.subscriptions.model import Subscription

class SubscriptionList(ResourceList):
	schema = SubscriptionSchema
	data_layer = { 'session': db.session,
			       'model': Subscription }

class SubscriptionDetail(ResourceDetail):
	schema = SubscriptionSchema
	data_layer = { 'session': db.session,
			       'model': Subscription }

class SubscriptionRelationship(ResourceRelationship):
	schema = SubscriptionSchema
	data_layer = { 'session': db.session,
			       'model': Subscription }
