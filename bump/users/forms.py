# TODO
"""User forms

This module contains WTForms used by user views.

TODO: renable TOS and recaptcha (templates)
"""

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Required, EqualTo, Email


class LoginForm(FlaskForm):
    """Login form"""

    email = StringField('Email address', [Required(), Email()])
    password = PasswordField('Password', [Required()])


class RegisterForm(FlaskForm):
    """ Registration form"""

    name = StringField('NickName', [Required()])
    email = StringField('Email address', [Required(), Email()])
    password = PasswordField('Password', [Required()])
    confirm = PasswordField('Repeat Password', [
        Required(),
        EqualTo('password', message='Passwords must match')
        ])
    # accept_tos = BooleanField('I accept the TOS', [Required()])
    # recaptcha = RecaptchaField()
