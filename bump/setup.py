from bump.users.views import MOD as usersModule
from bump import APP, DB


APP.register_blueprint(usersModule)


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
