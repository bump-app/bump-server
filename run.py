"""Starts Bump app

Initializes APP by running bump/__init__.py then bump/setup.py

"""

from bump import APP, DB, SERVER_BIND

APP.run(host=SERVER_BIND[0],
        port=SERVER_BIND[1])
