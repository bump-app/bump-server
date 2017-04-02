"""Starts Bump app

Initializes APP by running bump/__init__.py then bump/setup.py

"""

import sys
from bump import APP, DB, SERVER_BIND

def run():
    APP.run(host=SERVER_BIND[0],
            port=SERVER_BIND[1])

def initdb():
    """
    Creates the database tables.
    """
    print('Initializing database...')
    DB.create_all()
    print('Initialized the database.')
    print('Location: {path}'.format(
        path=APP.config['SQLALCHEMY_DATABASE_URI']))

if sys.argv[1] == 'initdb':
    initdb()
else:
    run()
