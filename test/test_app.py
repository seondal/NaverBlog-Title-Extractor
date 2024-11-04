# test_app.py
import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 테스트 클라이언트 생성
        cls.client = app.test_client()
        app.config['TESTING'] = True

    def test_hello_world(self):
        # /hello 엔드포인트 GET 요청 테스트
        response = self.client.get('/hello')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "Hello, World!")

    def test_add_numbers(self):
        # /add 엔드포인트 POST 요청 테스트
        response = self.client.post('/add', json={'a': 1, 'b': 2})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 3)

    @classmethod
    def tearDownClass(cls):
        # 테스트 종료 후 수행할 작업 (클라이언트 정리)
        pass

if __name__ == '__main__':
    unittest.main()
