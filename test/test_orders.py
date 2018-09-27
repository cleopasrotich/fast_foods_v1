from flask import Flask
import unittest
import json

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

    def test_postOrder(self):
        data  = {
            "price" : 500,
            "email" : "cleopasrotich81@gmail.com",
            "item"  : "pizza"
        }
        result = app.test_client()
        response= result.post('/fastfoods/api/v1/orders', data =json.dumps(data), content_type='application/json')
        self.assertTrue(response.status_code, 201)
        self.assertTrue(response.status_code, 200)
        self.assertTrue(response.status_code, 401)


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

    def test_specified_order(self):
        result = app.test_client()
        response= result.get('/fast_foods/api/v1/orders/<int:order_id>', content_type='application/json')
        self.assertTrue(response.status_code, 200)

    def test_empty_data(self):
        data = {}
        result = app.test_client()
        response= result.get('/fast_foods/api/v1/orders/<int:order_id>', data = json.dumps(data), headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 404)

    def test_status_order(self):
        data = {"status": "functional"}
        result = app.test_client()
        response= result.get('/fast_foods/api/v1/orders', data = json.dumps(data), headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 404)
        self.assertTrue(response.status_code, 200)
        self.assertTrue(response.status_code, 201)


if __name__ == '__main__':
    main()