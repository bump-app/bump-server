from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

class PostSchema(Schema):
	class Meta:
		type_ = 'post'
		self_view = 'post_detail'
		self_view_kwargs = {'id': '<id>'}
		self_view_many = 'post_list'

	id = fields.Integer(dump_only=True)
	created_at = fields.DateTime(dump_only=True)
	updated_at = fields.DateTime(dump_only=True)
	title = fields.String(required=True)
	text = fields.String(required=True)
	rating = fields.Integer(dump_only=True)
	user = Relationship(attribute='user',
						self_view='post_user',
						self_view_kwargs={'id': '<id>'},
						related_view='post_detail',
						related_view_kwargs={'id': '<id>'},
						schema='UserSchema',
						type_='user')
	channel = Relationship(attribute='channel',
						self_view='post_channel',
						self_view_kwargs={'id': '<id>'},
						related_view='post_detail',
						related_view_kwargs={'id': '<id>'},
						schema='ChannelSchema',
						type_='channel')
	comments = Relationship(self_view='post_comments',
							self_view_kwargs={'id': '<id>'},
							related_view='comment_list',
							related_view_kwargs={'id': '<id>'},
							many=True,
							schema='CommentSchema',
							type_='comment')
