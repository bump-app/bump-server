from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

class CommentSchema(Schema):
	class Meta:
		type_ = 'comment'
		self_view = 'comment_detail'
		self_view_kwargs = {'id': '<id>'}
		self_view_many = 'comment_list'

	id = fields.Integer(dump_only=True)
	text = fields.String(required=True)
	rating = fields.Integer(dump_only=True)
	created_at = fields.DateTime(dump_only=True)
	updated_at = fields.DateTime(dump_only=True)
	post = Relationship(attribute='post',
						self_view='comment_post',
						self_view_kwargs={'id': '<id>'},
						related_view='post_detail',
						related_view_kwargs={'id': '<id>'},
						schema='PostSchema',
						type_='post')
	user = Relationship(attribute='user',
						self_view='comment_user',
						self_view_kwargs={'id': '<id>'},
						related_view='user_detail',
						related_view_kwargs={'id': '<id>'},
						schema='UserSchema',
						type_='user')
