import unittest
from app.dataAccess.mongoData import mongoData

from unittest.mock import Mock, patch

from app import app
from json import dumps


# https://realpython.com/blog/python/testing-third-party-apis-with-mocks/
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
        mock_getAll.return_value = [{'url':'http://mock-server.com/rest/api', 'name': 'mock'}]

        # act
        response = self.app.get('/allData')

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertIn('some', response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
