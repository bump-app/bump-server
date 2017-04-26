from bump import DB as db
from bump.auth.client import Client
from bump.users.model import User
from bump.channels.model import Channel
from bump.posts.model import Post

def seed():
        test_client = Client( client_id="test",
                                                      secret="notverysecret",
                                                      name="test",
                                                      is_confidential="false",
                                                      _redirect_uris="dummyurl")
        db.session.add(test_client)

        # users
        matt = User(name="matthewdias",
                                email="matthewdias@asdf.com",
                                password="totallysecurepassword",
                                _role=1,
                                status=2)

        will = User(name="whitey",
                                email="will@asdf.com",
                                password="123",
                                _role=1,
                                status=2)

        # channels
        overwatch = Channel(name="overwatch",
                                                description="overwatch description")

        pad = Channel(name="pad",
                                                description="pad description")

        # posts
        p1 = Post(      link="https://www.youtube.com/watch?v=Qt5vWqSFC48",
                                text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                                user=matt,
                                channel=overwatch)

        p2 = Post(      link="https://www.youtube.com/watch?v=gdx8meu46EE",
                                text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                                user=will,
                                channel=pad)

        p3 = Post(      link="http://imgur.com/H6kfgP7",
                                text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                                user=will,
                                channel=pad)

        try:
                db.session.add(matt)
                db.session.add(will)
                db.session.add(overwatch)
                db.session.add(pad)
                db.session.add(p1)
                db.session.add(p2)
                db.session.add(p3)
                db.session.commit()
        except:
                db.session.rollback()
