"""Starts Bump app

Initializes APP by running bump/__init__.py then bump/setup.py

"""

from bump import APP, DB, SERVER_BIND

# This is needed to register blueprints and cli commands to APP
# bump/setup.py could be appended to bump/__init__,py but would cause cicular
# import and require import statements to be in the middle of the file

from bump import setup


APP.run(host=SERVER_BIND[0],
        port=SERVER_BIND[1])
