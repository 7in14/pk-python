import unittest

from app import app
from json import dumps


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

    def test_getDataSource_noId_404(self):
        response = self.app.get('/dataSource/')

        self.assertEqual(response.status_code, 404)

    def test_deleteDataSource_noId_404(self):
        response = self.app.delete('/dataSource/')

        self.assertEqual(response.status_code, 404)

    def test_addDataSources_badData_400(self):
        # arrange
        headers = [('Content-Type', 'application/json')]
        toInsert = {'url': 'http://google.com'}
        response = self.app.put(
            '/dataSource', data=dumps(toInsert), headers=headers)

        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
