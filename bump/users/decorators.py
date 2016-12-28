from functools import wraps

from flask import g, flash, redirect, url_for, request


def requires_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash('You need to be signed in for this page.')
            return redirect(url_for('users.login', next=request.path))
        return func(*args, **kwargs)
    return decorated_function
