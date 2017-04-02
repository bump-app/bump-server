import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_rest_jsonapi import Api

import bump.config as config

_BASEDIR = os.path.abspath(os.path.dirname(__file__))

SERVER_BIND = ('0.0.0.0', 8000)


def _init_flask():
    app = Flask(__name__)
    app.config.from_object(config)
    # app.config.from_envvar('YOURAPPLICATION_SETTINGS')

    # add database settings
    app.config.update(dict(
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(_BASEDIR,
                                                            'bump.db'),
        DATABASE_CONNECT_OPTIONS={},
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        ))
    return app


APP = _init_flask()
DB = SQLAlchemy(APP)

# resources
from bump.users.resource import UserList, UserDetail, UserRelationship
from bump.posts.resource import PostList, PostDetail, PostRelationship
from bump.comments.resource import CommentList, CommentDetail, CommentRelationship

# api/routes
api = Api(APP)

# users
api.route(UserList, 'user_list', '/users')
api.route(UserDetail, 'user_detail', '/users/<int:id>')
api.route(UserRelationship, 'user_posts', '/users/<int:id>/relationships/posts')
api.route(UserRelationship, 'user_comments', '/users/<int:id>/relationships/comments')

# posts
api.route(PostList, 'post_list', '/posts')
api.route(PostDetail, 'post_detail', '/posts/<int:id>')
api.route(PostRelationship, 'post_user', '/posts/<int:id>/relationships/user')
api.route(PostRelationship, 'post_comments', '/posts/<int:id>/relationships/comments')

# comments
api.route(CommentList, 'comment_list', '/comments')
api.route(CommentDetail, 'comment_detail', '/comments/<int:id>')
api.route(CommentRelationship, 'comment_user', '/comments/<int:id>/relationships/user')
api.route(CommentRelationship, 'comment_post', '/comments/<int:id>/relationships/post')
