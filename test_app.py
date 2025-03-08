import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, CI/CD!")

    def test_status_route(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "running", "message": "API is up and running!"})

if __name__ == '__main__':
    unittest.main()
