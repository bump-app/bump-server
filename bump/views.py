from flask import Blueprint, request, render_template, flash, g, session, \
    redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from bump import DB as db
from app.users.forms import RegisterForm, LoginForm
from app.users.models import User
from app.users.decorators import requires_login

mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/me/')
@requires_login
def home():
    return render_template("users/profile.html", user=g.user)



