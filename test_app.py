import unittest

from app import create_app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app, socketio = create_app('testing')
        self.ctx = self.app.app_context()
        self.client = socketio.test_client(self.app)

    def tearDown(self):
        pass

    def test_message(self):
        self.client.emit('David')
        received = self.client.get_received()
        print(received)

if __name__ == '__main__':
    unittest.main()
