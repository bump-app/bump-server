import os
import unittest
import tempfile

from flask import url_for

#import bump
from bump import APP, DB
#from bump import setup
from test.url import *

class BumpTestCase(unittest.TestCase):
    """Test cases for Bump."""

    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + self.db_path
        APP.config['TESTING'] = True
        APP.config['WTF_CSRF_ENABLED'] = False
        self.app = APP.test_client()
        with APP.app_context():
            #print('Initializing database...')
            DB.create_all()
            #print('Initialized the database.')
            #print('Location: {path}'.format(
                #path=APP.config['SQLALCHEMY_DATABASE_URI']))

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_empty_db(self):
        rv = self.app.get(INDEX_URL)
        assert b'No Posts!' in rv.data

    def register(self, name, email, password, confirm):
        return self.app.post(USERS_REGISTER_URL, data=dict(
            name=name,
            email=email,
            password=password,
            confirm=confirm
            ), follow_redirects=True)
    
    def login(self, email, password):
        return self.app.post(USERS_LOGIN_URL, data=dict(
            email=email,
            password=password
            ), follow_redirects=True)

    def logout(self):
        return self.app.get(USERS_LOGOUT_URL, follow_redirects=True)

    # TODO: need to test for unique nickname/email
    def test_register(self):
        rv = self.register('admin', 'admin@g.com', 'default', 'defaultx')
        assert b'Passwords must match' in rv.data
        rv = self.register('admin', 'admin@g.com', 'default', 'default')
        assert b'Thanks for registering!' in rv.data
        assert b'Hi admin!' in rv.data

    def test_login_logout(self):
        rv = self.register('admin', 'admin@g.com', 'default', 'default')
        rv = self.login('adminx@g.com', 'default')
        assert b'Wrong email or password' in rv.data
        rv = self.login('admin@g.com', 'defaultx')
        assert b'Wrong email or password' in rv.data

        rv = self.login('admin@g.com', 'default')
        assert b'Welcome admin!' in rv.data

        rv = self.logout()
        assert b'You were logged out.' in rv.data

    def post(self, title, text):
        return self.app.post(POSTS_NEW_POST_URL, data=dict(
            title=title,
            text=text
            ), follow_redirects=True)

    # TODO: figure out handling login status after registering
    def test_post(self):
        rv = self.register('admin', 'admin@g.com', 'default', 'default')
        rv = self.register('admin2', 'admin2@g.com', 'default', 'default')
        rv = self.login('admin@g.com', 'default')
        
        rv = self.post("test","test text")
        assert b'test text' in rv.data
        assert b'test | By: admin' in rv.data
        

        rv = self.logout()
        assert b'You were logged out.' in rv.data
        
        # second user posting
        rv = self.login('admin2@g.com', 'default')
        
        rv = self.post("test2","test text2")
        assert b'test text2' in rv.data
        assert b'test2 | By: admin' in rv.data
        
        # make sure first post is still there
        assert b'test text' in rv.data
        assert b'test | By: admin' in rv.data

        rv = self.logout()
        assert b'You were logged out.' in rv.data
