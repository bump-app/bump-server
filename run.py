from bump import APP, DB, SERVER_BIND
# This is needed to register blueprints and cli commands to APP
from bump import setup


APP.run(host=SERVER_BIND[0],
        port=SERVER_BIND[1])
