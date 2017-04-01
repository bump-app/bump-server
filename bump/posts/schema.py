from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

class PostSchema(Schema):
	class Meta:
		type_ = 'post'
		self_view = 'post_detail'
		self_view_kwargs = {'id': '<id>'}
		self_view_many = 'post_list'

    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    text = fields.String(required=True)
    rating = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    comment_count = fields.Integer(dump_only=True)
    comments = Relationship(self_view='post_comments',
    						self_view_kwargs={'id': '<id>'},
    						related_view='comment_list',
    						related_view_kwargs={'id': '<id>'},
    						many=True,
    						schema='CommentSchema',
    						type_='comment')
