from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

class ChannelSchema(Schema):
    class Meta:
        type_ = 'channel'
        self_view = 'channel_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'channel_list'

    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    name = fields.String(required=True)
    desc = fields.String(required=True)
    subscribers = Relationship(   self_view='channel_subscribers',
                            self_view_kwargs={'id': '<id>'},
                            related_view='subscription_list',
                            related_view_kwargs={'channel_id': '<id>'},
                            many=True,
                            schema='SubscriptionSchema',
                            type_='subscription')
    posts = Relationship(   self_view='channel_posts',
                            self_view_kwargs={'id': '<id>'},
                            related_view='post_list',
                            related_view_kwargs={'channel_id': '<id>'},
                            many=True,
                            schema='PostSchema',
                            type_='post')
