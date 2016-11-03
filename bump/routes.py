from bump import APP
from flask import render_template


# View functions
@APP.route('/')
def index():
    return render_template('index.html')
