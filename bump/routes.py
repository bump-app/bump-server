from flask import render_template


def index_view():
    """
    view function for the index page
    """
    return render_template('index.html')


# view func registry
VIEW_FUNCTIONS = (
    # url       function    options
    ('/',       index_view, {}),
    ('/index',  index_view, {}),
)
