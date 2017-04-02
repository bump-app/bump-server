import os

from flask import Flask
from flask_cors import CORS
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
CORS(APP)

from bump.routes import Route

API = Api(APP)
Route(API)
