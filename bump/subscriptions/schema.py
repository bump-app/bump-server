from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

class SubscriptionSchema(Schema):
    class Meta:
        type_ = 'subscriptions'
        self_view = 'subscription_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'subscription_list'

    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    user = Relationship(attribute='user',
                        self_view='subscription_user',
                        self_view_kwargs={'id': '<id>'},
                        related_view='subscription_detail',
                        related_view_kwargs={'id': '<id>'},
                        schema='UserSchema',
                        type_='user')
    channel = Relationship(attribute='channel',
                        self_view='subscription_channel',
                        self_view_kwargs={'id': '<id>'},
                        related_view='subscription_detail',
                        related_view_kwargs={'id': '<id>'},
                        schema='ChannelSchema',
                        type_='channel')
