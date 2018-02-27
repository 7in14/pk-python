import unittest
from unittest.mock import patch, Mock
from json import dumps
from json.decoder import JSONDecodeError
from requests.exceptions import ConnectionError

from app import app
from app.dataAccess.mongoData import mongoData


class AllDataTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

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

    @patch('app.allData.requests.get')
    @patch.object(mongoData, 'get_all')
    def test_allDataMocked_JSONDecodeError(self, mock_getAll, mock_get):
        # arrange
        mock_get.side_effect = JSONDecodeError('could not parse json', 'doc', 1)
        mock_getAll.return_value = [
            {'url': 'http://mock-server.com/rest/api', 'name': 'mock'}]

        # act
        response = self.app.get('/allData')

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertIn(f"could not json parse response from http://mock-server.com/rest/api", response.get_data(as_text=True))

    @patch('app.allData.requests.get')
    @patch.object(mongoData, 'get_all')
    def test_allDataMocked_ConnectionError(self, mock_getAll, mock_get):
        # arrange
        mock_get.side_effect = ConnectionError('server not responding')
        mock_getAll.return_value = [
            {'url': 'http://mock-server.com/rest/api', 'name': 'mock'}]

        # act
        response = self.app.get('/allData')

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertIn(f"could not connect to remote server: http://mock-server.com/rest/api", response.get_data(as_text=True))
