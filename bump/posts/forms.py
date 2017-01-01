"""Post forms

This module contains WTForms used by post views.

"""

from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required


class NewPostForm(FlaskForm):
    """New post form"""

    title = TextField('Title', [Required()])
    text = TextField('Text')


class NewCommentForm(FlaskForm):
    """New comment form"""

    text = TextField('Text', [Required()])
