import unittest

from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass


    def test_helloWorld(self):
        response = self.app.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')


    def test_ping(self):
        response = self.app.get('/ping')

        self.assertEqual(response.data, b'pong')


    def test_file(self):
        response = self.app.get('/file')

        self.assertIn(b'Simple python web app built with flask', response.data)


    def test_crime(self):
        response = self.app.get('/raleigh/crime')

        self.assertEqual(response.status_code, 200)


    def test_crimeWithQuery(self):
        response = self.app.get('/raleigh/crime?query=Drug')

        self.assertEqual(response.status_code, 200)


    def test_allData(self):
        response = self.app.get('/allData')

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
