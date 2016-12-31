"""Initializes the flask app and database

Loads condig from config.py

Initializes APP, DB, and SERVER_BIND

"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import bump.config as config

_BASEDIR = os.path.abspath(os.path.dirname(__file__))

SERVER_BIND = ('0.0.0.0', 8000)


def _init_flask():
    """Flask configuration"""

    app = Flask(__name__)

    # base config from config.py
    app.config.from_object(config)
    # app.config.from_envvar('YOURAPPLICATION_SETTINGS')

    # add database settings
    app.config.update(dict(
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(_BASEDIR,
                                                            'bump.db'),
        DATABASE_CONNECT_OPTIONS={},
        # explicitly set to remove warning
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        ))
    return app


APP = _init_flask()
DB = SQLAlchemy(APP)