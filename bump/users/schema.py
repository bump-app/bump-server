from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

class UserSchema(Schema):
    class Meta:
        type_ = 'user'
        self_view = 'user_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'user_list'

    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)
    _role = fields.Integer(dump_only=True)
    status = fields.Integer(dump_only=True)
    subscriptions = Relationship(   self_view='user_subscriptions',
                                    self_view_kwargs={'id': '<id>'},
                                    related_view='subscription_list',
                                    related_view_kwargs={'user_id': '<id>'},
                                    many=True,
                                    schema='SubscriptionSchema',
                                    type_='subscription')
    posts = Relationship(   self_view='user_posts',
                            self_view_kwargs={'id': '<id>'},
                            related_view='post_list',
                            related_view_kwargs={'user_id': '<id>'},
                            many=True,
                            schema='PostSchema',
                            type_='post')
    comments = Relationship(self_view='user_comments',
                            self_view_kwargs={'id': '<id>'},
                            related_view='comment_list',
                            related_view_kwargs={'id': '<id>'},
                            many=True,
                            schema='CommentSchema',
                            type_='comment')
