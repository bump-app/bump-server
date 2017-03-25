# TODO
"""Post views

This module contrains post views exported using Blueprint.


TODO: make sure to check the user to make sure they are deleting their own
posts and comments and not someone else's
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


@MOD.route('/')
@MOD.route('/posts/')
def all_posts():
    """Post view

    Displays all posts made by all users.

    """
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


@MOD.route('/new_post/', methods=['GET', 'POST'])
@requires_login
def new_post():
    """New post view

    Form to make a new post. Must be logged in.

    """
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


@MOD.route('/posts/del_post/<post_id>/')
@requires_login
def delete_post(post_id):
    """Deletes a post

    Uses cascading to delete all comments belonging to the post.

    """
    post = Post.query.filter_by(id=post_id).first()

    # make sure the post exist
    if post:
        # delete the post from database and commit
        db.session.delete(post)
        db.session.commit()

        flash("Post deleted!")
    return redirect(url_for('posts.all_posts'))


@MOD.route('/posts/<post_id>/', methods=['GET', 'POST'])
def all_comments(post_id):
    """Comments view

    Displays all comments belonging to a single post.

    Also displays the post as well as a form to make new comments if logged in.
    """
    form = NewCommentForm(request.form)

    post = Post.query.filter_by(id=post_id).first()

    # make sure the post exists
    if post:
        # process the new comment form if the data is valid
        if form.validate_on_submit():
            # create a new comment
            comment = Comment(text=form.text.data, post_id=post_id,
                              user_id=g.user.id)

            # insert the comment in database and commit it
            db.session.add(comment)
            db.session.commit()
            flash("Comment posted!")

        # get the comments after potentially inserting the new comment so that
        # the user can see the new comment just made
        comments = post.comments.all()
        return render_template("posts/all_comments.html", post=post,
                               comments=comments, form=form)
    return redirect(url_for('posts.all_posts'))


@MOD.route('/posts/<post_id>/del_comment/<comment_id>/')
@requires_login
def delete_comment(post_id, comment_id):
    """Deletes a comment"""

    post = Post.query.filter_by(id=post_id).first()
    # make sure the post still exists
    if post:
        comment = post.comments.filter_by(id=comment_id).first()
        # make sure the comment still exists
        if comment:
            # delete the comment from database and commit
            db.session.delete(comment)
            db.session.commit()
            flash("Comment deleted!")

        return redirect(url_for('posts.all_comments', post_id=post.id))
    return redirect(url_for('posts.all_posts'))
