#!/usr/bin/python3
from flask import Flask, render_template

import os
import sqlite3


# Flask configuration
def _init_flask():
    app = Flask(__name__)
    # base config
    app.config.from_object(__name__)
    # add database settings
    app.config.update({})
    return app


app = _init_flask()


# View functions
@app.route('/')
def index():
    return render_template('index.html')


# runner
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
