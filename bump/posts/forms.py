"""Post forms

This module contains WTForms used by post views.

"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Required


class NewPostForm(FlaskForm):
    """New post form"""

    title = StringField('Title', [Required()])
    text = StringField('Text')


class NewCommentForm(FlaskForm):
    """New comment form"""

    text = StringField('Text', [Required()])
