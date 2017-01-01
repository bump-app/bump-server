"""Post views

This module contrains post views exported using Blueprint.

"""

from flask import Blueprint, request, render_template, flash, g, session, \
    redirect, url_for

from bump import DB as db
from bump.posts.forms import NewPostForm, NewCommentForm
from bump.posts.models import Post, Comment
# from bump.posts.decorators import

# FIXME user import in posts
from bump.users.decorators import requires_login
from bump.users.models import User

MOD = Blueprint('posts', __name__)


@MOD.route('/posts/')
def all_posts():
    """Post view"""

    posts = Post.query.all()
    return render_template("posts/all_posts.html", posts=posts)


@MOD.before_request
def before_request():
    """

    Pull user's profile from the database before every request are treated.

    NOTE: should cache this later

    """
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


# FIXME <username>
# @MOD.route('/<username>/new_post/', methods=['GET', 'POST'])
@MOD.route('/new_post/', methods=['GET', 'POST'])
@requires_login
# def new_post(username):
def new_post():
    """New post view"""

    form = NewPostForm(request.form)

    # make sure data are valid
    if form.validate_on_submit():
        post = Post(title=form.title.data, text=form.text.data,
                    user_id=session['user_id'])

        # insert the post in database and commit it
        db.session.add(post)
        db.session.commit()

        flash("Posted!")

        return redirect(url_for('posts.all_posts'))
    return render_template("posts/new_post.html", form=form)


@MOD.route('/comments/<post_id>/', methods=['GET', 'POST'])
def all_comments(post_id):
    """Comments view"""

    form = NewCommentForm(request.form)

    post = Post.query.filter_by(id=post_id).first()

    # make sure data are valid
    if form.validate_on_submit():
        comment = Comment(text=form.text.data, post_id=post_id,
                          user_id=post.user.id)

        db.session.add(comment)
        db.session.commit()

        flash("Comment posted!")

    comments = post.comments.all()
    return render_template("posts/all_comments.html", post=post,
                           comments=comments, form=form)
