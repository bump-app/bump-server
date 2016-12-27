from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#FIXME
from flask_security import Security, SQLAlchemyUserDatastore
import os
        
_basedir = os.path.abspath(os.path.dirname(__file__))

#import bump.users
SERVER_BIND = ('0.0.0.0', 8000)


# Flask configuration
def _init_flask():
    app = Flask(__name__)
    # base config
    app.config.from_object(__name__)
    #app.config.from_object('yourapplication.default_settings')
    #app.config.from_envvar('YOURAPPLICATION_SETTINGS')

    # add database settings
    app.config.update(dict(
        SQLALCHEMY_DATABASE_URL = 'sqlite:///' + os.path.join(_basedir,
        'bump.db'),
        DATABASE_CONNECT_OPTIONS = {},
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        
        WTF_CSRF_ENABLED = True,
        WTF_CSRF_SECRET_KEY = "somethingimpossibletoguess",

        RECAPTCHA_USE_SSL = False,
        RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J',
        RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu',
        RECAPTCHA_OPTIONS = {'theme': 'white'},

        SECURITY_REGISTER_URL = '/register/',

        SECRET_KEY = 'secret key'))
    #FIXME add secret key in config
    return app


APP = _init_flask()
DB = SQLAlchemy(APP)
# XXX dont know the best way to fix circular dependency in init
# the models need DB but user_datastore need the models
from bump.users.models import User, Role
user_datastore = SQLAlchemyUserDatastore(DB, User, Role)
security = Security(APP, user_datastore)
