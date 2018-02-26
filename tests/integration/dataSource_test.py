import unittest
import os

from app import app, get_mongo
from mockupdb import MockupDB, go, Command
from pymongo import MongoClient
from mockupdb._bson import ObjectId as mockup_oid
from json import dumps


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
            Command({'find': 'dataSources', 'filter': {'_id': mockup_oid('5a8f1e368f7936badfbb0cfa')}, 'limit': 1, 'singleBatch': True}, flags=4, namespace='app'))
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
            Command({'find': 'dataSources', 'filter': {'_id': mockup_oid('5a8f1e368f7936badfbb0cfb')}, 'limit': 1, 'singleBatch': True}, flags=4, namespace='app'))
        request.ok(cursor={'id': 0, 'firstBatch': []})

        # act
        http_response = future()

        # assert
        self.assertEqual(http_response.status_code, 404)

    def test_getDataSources(self):
        # arrange
        future = go(self.app.get, '/dataSources')
        request = self.server.receives(
            Command({'find': 'dataSources', 'filter': {}}, flags=4, namespace='app'))
        request.ok(cursor={'id': 0, 'firstBatch': [
            {'name': 'Google', 'url': 'http://google.com/rest/api'},
            {'name': 'Rest', 'url': 'http://rest.com/rest/api'}]})

        # act
        http_response = future()

        # assert
        data = http_response.get_data(as_text=True)
        self.assertIn('http://google.com/rest/api', data)
        self.assertIn('http://rest.com/rest/api', data)

    def test_addDataSource(self):
        # arrange
        id = '5a924d7a29a6e5484dcf68be'
        headers = [('Content-Type', 'application/json')]
        #   need to pass _id because pymongo creates one so it's impossible to match insert request without _ids
        toInsert = {'name': 'new', 'url': 'http://google.com',
                    '_id': id}
        future = go(self.app.put, '/dataSource',
                    data=dumps(toInsert), headers=headers)
        request = self.server.receives(
            Command({'insert': 'dataSources', 'ordered': True, 'documents': [{'name': 'new', 'url': 'http://google.com',
                                                                              '_id': mockup_oid(id)}]}, namespace='app'))
        request.ok(cursor={'inserted_id': id})

        # act
        http_response = future()

        # assert
        data = http_response.get_data(as_text=True)
        self.assertIn(id, data)
        self.assertEqual(http_response.status_code, 201)

    def test_deleteDataSource(self):
        # arrange
        id = '5a8f1e368f7936badfbb0cfa'
        future = go(self.app.delete, f'/dataSource/{id}')
        request = self.server.receives(
            Command({'delete': 'dataSources', 'ordered': True, 'deletes': [{'q': {'_id': mockup_oid(id)}, 'limit': 1}]}, namespace='app'))
        request.ok({'acknowledged': True, 'n': 1})

        # ackwoledged:  True
        # 	raw_result:  {'n': 1, 'ok': 1.0}
        # 	deleted_count:  1

        # act
        http_response = future()

        # assert
        self.assertIn(f'deleted {id}',
                      http_response.get_data(as_text=True))
        self.assertEqual(http_response.status_code, 202)
