import unittest
import os

from app import app, get_mongo
from mockupdb import MockupDB, go, Command
from pymongo import MongoClient
from mockupdb._bson import ObjectId as mockup_oid


class GetDataSourceTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.server = MockupDB(auto_ismaster=True, verbose=True)
        self.server.run()
        # create mongo connection to mock server
        print('calling get_mongo with ' + self.server.uri)
        client = get_mongo(self.server.uri)

        app.testing = True
        self.app = app.test_client()

    @classmethod
    def tearDownClass(self):
        self.server.stop()

    def test_getDataSource(self):
        # arrange
        future = go(self.app.get, '/dataSource/5a8f1e368f7936badfbb0cfa')
        request = self.server.receives(
            Command({"find": "dataSources", "filter": {"_id": mockup_oid('5a8f1e368f7936badfbb0cfa')}, "limit": 1, "singleBatch": True}, flags=4, namespace="app"))
        request.ok(cursor={'id': 0, 'firstBatch': [
            {'name': 'bla', 'url': 'http://google.com/rest/api'}]})

        # act
        http_response = future()

        # assert
        self.assertIn('http://google.com/rest/api',
                      http_response.get_data(as_text=True))

    def test_getDataSource_404(self):
        future = go(self.app.get, '/dataSource/5a8f1e368f7936badfbb0cfb')
        request = self.server.receives(
            Command({"find": "dataSources", "filter": {"_id": mockup_oid('5a8f1e368f7936badfbb0cfb')}, "limit": 1, "singleBatch": True}, flags=4, namespace="app"))
        request.ok(cursor={'id': 0, 'firstBatch': []})

        # act
        http_response = future()

        # assert
        self.assertEqual(http_response.status_code, 404)
