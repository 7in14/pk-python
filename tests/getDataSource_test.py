import unittest
import os

from app import app, get_Mongo
from mockupdb import MockupDB, go, Command
from pymongo import MongoClient
from mockupdb._bson import ObjectId as mockup_oid


class GetDataSourceTestCase(unittest.TestCase):

    def setUp(self):
        self.server = MockupDB(auto_ismaster=True, verbose=True)
        self.server.run()
        # create mongo connection to mock server
        print('calling get_Mongo with ' + self.server.uri)
        client = get_Mongo(self.server.uri)

        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        self.server.stop()

    def test_getDataSource(self):
        future = go(self.app.get, '/dataSource/5a8f1e368f7936badfbb0cfa')
        # request = self.server.receives(
        #     Command({'find': 'dataSources', 'filter': {'_id': {'$oid': mockup_oid('5a8f1e368f7936badfbb0cfa')}}, 'limit': 1, 'singleBatch': True}, flags=4, namespace='app'))

        request = self.server.receives(
            Command({"find": "dataSources", "filter": {"_id": mockup_oid('5a8f1e368f7936badfbb0cfa')}, "limit": 1, "singleBatch": True}, flags=4, namespace="app"))

        request.ok(cursor={'id': 0, 'firstBatch': [
            {'name': 'bla', 'url': 'http://google.com/rest/api'}]})
        http_response = future()

        self.assertIn('http://google.com/rest/api',
                      http_response.get_data(as_text=True))
