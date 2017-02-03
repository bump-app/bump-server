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

# loads in the Blueprint
from bump.users.views import MOD as usersModule
from bump.posts.views import MOD as postsModule

APP.register_blueprint(usersModule)
APP.register_blueprint(postsModule)


# create the db using flask's built in cli
@APP.cli.command('initdb')
def initdb_command():
    """
    Creates the database tables.
    """
    print('Initializing database...')
    DB.create_all()
    print('Initialized the database.')
    print('Location: {path}'.format(
        path=APP.config['SQLALCHEMY_DATABASE_URI']))
