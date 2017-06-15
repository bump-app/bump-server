from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from flask_mail import Message

from bump import DB as db
from bump import MAIL as mail
from bump.users.schema import UserSchema
from bump.users.model import User


# FIXME move mail related methods out
def send_confirmation(user):
    #with mail.record_messages() as outbox:
    msg = Message("confirmation from bump", recipients=[user['email']])
    msg.body = "temp"
    msg.html = "<b>will add confirmation link later</b>"
    mail.send(msg)
        #print(outbox[0], file=sys.stderr)

def after_create_object(self, obj, data, view_kwargs):
    send_confirmation(obj)

class UserList(ResourceList):
	schema = UserSchema
	data_layer = { 'session': db.session,
                   'model': User,
                   'after_create_object': after_create_object }
	# get_decorators = [oauth2.require_oauth('list_user')]

class UserDetail(ResourceDetail):
	schema = UserSchema
	data_layer = { 'session': db.session,
				   'model': User }

class UserRelationship(ResourceRelationship):
	schema = UserSchema
	data_layer = { 'session': db.session,
				   'model': User }
