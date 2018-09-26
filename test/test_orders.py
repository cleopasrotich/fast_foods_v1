from flask import Flask
import unittest

app = Flask(__name__)


class Testorders(unittest.TestCase):

    def test_all(self):
        result = app.test_client()
        response = result.get('/fast_foods/api/v1/orders',content_type='application/json')
        self.assertTrue(response.status_code, 200)

    def test_all_orders(self):
        result = app.test_client()
        response = result.get('/fast_foods/api/v1/orders', content_type='application/json')
        self.assertTrue(response.status_code, 200)

    def test_edit_order(self):
        result = app.test_client()
        response = result.post('/fast_foods/api/v1/orders',  content_type='application/json')
        self.assertTrue(response.status_code, 200)

    def test_update_order(self):
        result = app.test_client()
        response = result.get('/fast_foods/api/v1/orders/2', content_type='application/json')
        self.assertTrue(response.status_code, 200)

    def test_remove_order(self):
        result = app.test_client()
        response = result.get('/fast_foods/api/v1/orders/2', content_type='application/json')
        self.assertTrue(response.status_code, 200)


