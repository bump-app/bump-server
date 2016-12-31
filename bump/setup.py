"""Performs setup on the app

Loads Blueprints in to flask app and initialize the database using the cli
built in.

"""

from bump import APP, DB
# loads in the Blueprint
from bump.users.views import MOD as usersModule
from bump.posts.views import MOD as postsModule

APP.register_blueprint(usersModule)
APP.register_blueprint(postsModule)


# create the db using flask's built in cli
@APP.cli.command('initdb')
def initdb_command():
    """
    Creates the database tables.
    """
    print('Initializing database...')
    DB.create_all()
    print('Initialized the database.')
    print('Location: {path}'.format(
        path=APP.config['SQLALCHEMY_DATABASE_URI']))
