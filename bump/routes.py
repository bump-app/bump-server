from flask import render_template, url_for


def index_view():
    """
    view function for the index page
    """
    return render_template('index.html')

def register():
    """
    view function for the registration page
    """
    pass

def login():
    """
    view function for the login page
    """
    pass

def logout():
    """
    view function for the logout page
    """
    pass


# view func registry
VIEW_FUNCTIONS = (
    # url          function      options
    ('/',          index_view,   {}),
    ('/index/',    index_view,   {}),
    ('/login/',    login,        {}),
    ('/logout/',   logout,       {}),
    ('/register/', register,     {}),
)
