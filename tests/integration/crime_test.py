import unittest
import json
from unittest.mock import Mock, patch

from app import app


# https://realpython.com/blog/python/testing-third-party-apis-with-mocks/
class CrimeTestCase(unittest.TestCase):

    crimeData = [{
        'district': 'SOUTHEAST',
        'inc_datetime': '2018-02-02T00:00:00.000',
        'lcr': '71A',
        'lcr_desc': 'Traffic/DWI (Driving While Impaired)',
    }, {
        'district': 'SOUTHWEST',
        'inc_datetime': '2018-02-02T00:39:00.000',
        'lcr': '54D',
        'lcr_desc': 'Drug Violation/Misdemeanor',
    }]

    def json_of_response(self, response):
        return json.loads(response.data.decode('utf8'))

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    @patch('app.allData.requests.get')
    def test_crime_filtered(self, mock_get):
        # arrange
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = self.crimeData

        # act
        response = self.app.get('/raleigh/crime?query=Drug')
        jsonResponse = self.json_of_response(response)

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Drug Violation/Misdemeanor',
                         jsonResponse[0]['lcr_desc'])

    @patch('app.allData.requests.get')
    def test_crime_all(self, mock_get):
        # arrange
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = self.crimeData

        # act
        response = self.app.get('/raleigh/crime')
        jsonResponse = self.json_of_response(response)

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(2, len(jsonResponse))


if __name__ == '__main__':
    unittest.main()
