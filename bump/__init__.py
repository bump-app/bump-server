import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import bump.config
        
_basedir = os.path.abspath(os.path.dirname(__file__))

SERVER_BIND = ('0.0.0.0', 8000)


# Flask configuration
def _init_flask():
    app = Flask(__name__)

    # base config
    app.config.from_object(config)
    #app.config.from_envvar('YOURAPPLICATION_SETTINGS')

    # add database settings
    app.config.update(dict(
        SQLALCHEMY_DATABASE_URL = 'sqlite:///' + os.path.join(_basedir,
                                'bump.db'),
        DATABASE_CONNECT_OPTIONS = {},
        # explicitly set to remove warning
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        ))
    return app


APP = _init_flask()
DB = SQLAlchemy(APP)

# import blueprints
from bump.users.views import mod as usersModule
APP.register_blueprint(usersModule)
