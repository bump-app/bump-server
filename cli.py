import sys
from bump import APP, DB, SERVER_BIND

def run():
    APP.run(host=SERVER_BIND[0],
            port=SERVER_BIND[1])

def initdb():
    print('Initializing database...')
    DB.create_all()
    print('Initialized the database.')
    print('Location: {path}'.format(
        path=APP.config['SQLALCHEMY_DATABASE_URI']))

if sys.argv[1] == 'initdb':
    initdb()
else:
    run()
