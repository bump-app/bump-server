import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_rest_jsonapi import Api
from flask_oauthlib.provider import OAuth2Provider
from flask_mail import Mail

import bump.config as config

SERVER_BIND = ('0.0.0.0', 80)

APP = Flask(__name__, template_folder='templates')
APP.config.from_object(config)
# app.config.from_envvar('YOURAPPLICATION_SETTINGS')

APP.config.update(dict(
    SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL'],
    DATABASE_CONNECT_OPTIONS={},
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    # flask-mail config
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    #MAIL_DEBUG=,
    MAIL_USERNAME='noreply.bumpapp@gmail.com',
    MAIL_PASSWORD='Bumpapp1234',
    MAIL_DEFAULT_SENDER='noreply.bumpapp@gmail.com'
    #MAIL_MAX_EMAILS=,
    #MAIL_SUPPRESS_SEND=,
    #MAIL_ASCII_ATTACHMENTS=

    ))

DB = SQLAlchemy(APP)
CORS(APP)

api = Api(APP)
oauth2 = OAuth2Provider(APP)

MAIL = Mail(APP)

#def permission_manager(view, view_args, view_kwargs, *args, **kwargs):
    #"""The function use to check permissions

    #:param callable view: the view
    #:param list view_args: view args
    #:param dict view_kwargs: view kwargs
    #:param list args: decorator args
    #:param dict kwargs: decorator kwargs
    #"""
    #import sys
    #print("testing permissiuons", file=sys.stderr)

#api.permission_manager(permission_manager)

from bump.routes import Route

Route(api)
