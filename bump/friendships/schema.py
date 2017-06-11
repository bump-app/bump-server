from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

class FriendshipSchema(Schema):
    class Meta:
        type_ = 'friendships'
        self_view = 'friendship_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'friendship_list'

    id = fields.Integer(dump_only=True)
    confirmed = fields.Boolean()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    user = Relationship(attribute='user',
                        self_view='friendship_user',
                        self_view_kwargs={'id': '<id>'},
                        related_view='friendship_detail',
                        related_view_kwargs={'id': '<id>'},
                        schema='UserSchema',
                        type_='users')
    friend = Relationship(attribute='friend',
                          self_view='friendship_friend',
                          self_view_kwargs={'id': '<id>'},
                          related_view='friendship_detail',
                          related_view_kwargs={'id': '<id>'},
                          schema='UserSchema',
                          type_='users')
