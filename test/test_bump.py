import os
import unittest
import tempfile

#import bump
from bump import APP, DB
from bump import setup

class BumpTestCase(unittest.TestCase):
    """Test cases for Bump."""


    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + self.db_path
        APP.config['TESTING'] = True
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
        rv = self.app.get('/')
        assert b'No Posts!' in rv.data
    
