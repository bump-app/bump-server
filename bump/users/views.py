"""User views

This module contains user views exported using Blueprint.

"""

from flask import Blueprint, request, render_template, flash, g, session, \
    redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from bump import DB as db
from bump.users.forms import RegisterForm, LoginForm
from bump.users.models import User
from bump.users.decorators import requires_login

MOD = Blueprint('users', __name__)


@MOD.route('/')
@MOD.route('/me/')
@requires_login
def home():
    """Profile view"""
    return render_template("users/profile.html", user=g.user)


@MOD.before_request
def before_request():
    """

    Pull user's profile from the database before every request are treated.

    NOTE: should cache this later

    """
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


@MOD.route('/register/', methods=['GET', 'POST'])
def register():
    """Registration view"""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        # create an user instance not yet stored in the database
        user = User(name=form.name.data, email=form.email.data,
                    password=generate_password_hash(form.password.data))
        # insert the record in database and commit it
        db.session.add(user)
        db.session.commit()

        # Log the user in, as he now has an id
        session['user_id'] = user.id

        # flash a message to the user
        flash("Thanks for registering")
        # redirect user to the 'home' method of the user module
        return redirect(url_for('users.home'))
    return render_template("users/register.html", form=form)


@MOD.route('/login/', methods=['GET', 'POST'])
def login():
    """Login view"""
    form = LoginForm(request.form)

    # make sure data are valid but doesn't validate password
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # use werkzeug to validate user's password
        if user and check_password_hash(user.password, form.password.data):
            # the session can't be modified as it's signed,
            # it's a safe place to store the user id
            session['user_id'] = user.id
            flash("Welcome {username}!".format(username=user.name))
            return redirect(url_for('users.home'))
        flash("Wrong email or password", 'error-message')
    return render_template("users/login.html", form=form)


@MOD.route('/logout/')
def logout():
    """Logout view"""

    session.pop('user_id', None)
    flash("You were logged out.")
    return redirect(url_for('users.login'))
