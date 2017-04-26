import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_rest_jsonapi import Api
from flask_oauthlib.provider import OAuth2Provider, OAuth2RequestValidator

import bump.config as config

SERVER_BIND = ('0.0.0.0', 80)

APP = Flask(__name__, template_folder='templates')
APP.config.from_object(config)
# app.config.from_envvar('YOURAPPLICATION_SETTINGS')

APP.config.update(dict(
    SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL'],
    DATABASE_CONNECT_OPTIONS={},
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    ))

DB = SQLAlchemy(APP)
CORS(APP)

api = Api(APP)
oauth2 = OAuth2Provider(APP)

#class MyValidator(OAuth2RequestValidator):
    #def authenticate_client_id(client_id, request, *args, **kwargs):
        #request.client.client_id = client_id

    #def authenticate_client(request, *args, **kwargs):
        #request.client.client_id = 'test'

import bump.auth
#from bump.auth import load_client, load_token, load_grant

#oauth2._validator = MyValidator(load_client, load_token, load_grant)
api.oauth_manager(oauth2)

from bump.routes import Route

Route(api)
