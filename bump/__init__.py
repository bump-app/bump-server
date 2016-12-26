from flask import Flask, url_for

SERVER_BIND = ('0.0.0.0', 8000)


# Flask configuration
def _init_flask():
    app = Flask(__name__)
    # base config
    app.config.from_object(__name__)
    # add database settings
    app.config.update({})
    return app


APP = _init_flask()
