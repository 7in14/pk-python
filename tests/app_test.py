import unittest

import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def tearDown(self):
        print('Nothing to do here')

if __name__ == '__main__':
    unittest.main()
