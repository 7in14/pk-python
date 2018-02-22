import unittest
import os

from pytest_mongodb import plugin
from app import app, getMongo
from mockupdb import MockupDB

class GetDataSourceTestCase(unittest.TestCase):

    def setUp(self):
        self.server = MockupDB(auto_ismaster=True, verbose=True)
        self.server.run()
        # create mongo connection to mock server
        print('calling getMongo with ' + self.server.uri)
        getMongo(self.server.uri)

        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        self.server.stop()

    def test_getDataSource(self):
        response = self.app.get('/dataSource/5a8f1e368f7936badfbb0cfa')

        self.assertEqual(response.status_code, 404)
