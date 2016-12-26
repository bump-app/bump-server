from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
        SQLALCHEMY_TRACK_MODIFICATIONS = False))
    #FIXME secret key?
    print(__name__)
    return app


APP = _init_flask()
DB = SQLAlchemy(APP)
