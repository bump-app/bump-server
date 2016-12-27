from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import bump.config
#FIXME
#import os
        
#_basedir = os.path.abspath(os.path.dirname(__file__))

SERVER_BIND = ('0.0.0.0', 8000)


# Flask configuration
def _init_flask():
    app = Flask(__name__)
    # base config
    #app.config.from_object(__name__)
    app.config.from_object(config)
    #app.config.from_object('yourapplication.default_settings')
    #app.config.from_envvar('YOURAPPLICATION_SETTINGS')

    # add database settings
    #app.config.update(dict(
        #SQLALCHEMY_DATABASE_URL = 'sqlite:///' + os.path.join(_basedir,
        #'bump.db'),
        #DATABASE_CONNECT_OPTIONS = {},
        #SQLALCHEMY_TRACK_MODIFICATIONS = False,
        
        #WTF_CSRF_ENABLED = True,
        #WTF_CSRF_SECRET_KEY = "somethingimpossibletoguess",

        #RECAPTCHA_USE_SSL = False,
        #RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J',
        #RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu',
        #RECAPTCHA_OPTIONS = {'theme': 'white'},

        #SECURITY_REGISTER_URL = '/register/',

        #SECRET_KEY = 'secret key'))
    return app


APP = _init_flask()
DB = SQLAlchemy(APP)
