import unittest
import os

from app import app
from app.dataAccess.mongoData import mongoData

from mockupdb import MockupDB, go, Command
from pymongo import MongoClient
from mockupdb._bson import ObjectId as mockup_oid
from json import dumps
from unittest.mock import patch, Mock


class GetDataSourceTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.server = MockupDB(auto_ismaster=True, verbose=True)
        self.server.run()
        # create mongo connection to mock server

        app.testing = True
        app.config['MONGO_URI'] = self.server.uri
        self.app = app.test_client()

    @classmethod
    def tearDownClass(self):
        self.server.stop()

    def test_getDataSource(self):
        # arrange
        id = '5a8f1e368f7936badfbb0cfa'
        future = go(self.app.get, f'/dataSource/{id}')
        request = self.server.receives(
            Command({'find': 'dataSources', 'filter': {'_id': mockup_oid(id)}, 'limit': 1, 'singleBatch': True}, flags=4, namespace='app'))
        request.ok(cursor={'id': 0, 'firstBatch': [
            {'name': 'bla', 'url': 'http://google.com/rest/api'}]})

        # act
        http_response = future()

        # assert
        self.assertIn('http://google.com/rest/api',
                      http_response.get_data(as_text=True))

    def test_getDataSource_404(self):
        id = '5a8f1e368f7936badfbb0cfb'
        future = go(self.app.get, f'/dataSource/{id}')
        request = self.server.receives(
            Command({'find': 'dataSources', 'filter': {'_id': mockup_oid(id)}, 'limit': 1, 'singleBatch': True}, flags=4, namespace='app'))
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

        # act
        http_response = future()

        # assert
        self.assertIn(f'deleted {id}',
                      http_response.get_data(as_text=True))
        self.assertEqual(http_response.status_code, 202)

    def test_deleteDataSource_notFound(self):
        # arrange
        id = '5a8f1e368f7936badfbb0000'
        future = go(self.app.delete, f'/dataSource/{id}')
        request = self.server.receives(
            Command({'delete': 'dataSources', 'ordered': True, 'deletes': [{'q': {'_id': mockup_oid(id)}, 'limit': 1}]}, namespace='app'))
        request.ok({'acknowledged': True, 'n': 0})

        # act
        http_response = future()

        # assert
        self.assertIn(f'{id} not found',
                      http_response.get_data(as_text=True))
        self.assertEqual(http_response.status_code, 404)

    @patch('app.allData.requests.get')
    @patch.object(mongoData, 'get_all')
    def test_allDataMocked(self, mock_getAll, mock_get):
        # arrange
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = {'some': 'data'}
        mock_getAll.return_value = [
            {'url': 'http://mock-server.com/rest/api', 'name': 'mock'}]

        # act
        response = self.app.get('/allData')

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertIn('some', response.get_data(as_text=True))
