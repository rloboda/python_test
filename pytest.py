import unittest
from unittest.mock import patch
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_all_products(self):
        response = self.app.get('/api/products')
        self.assertEqual(response.status_code, 200)
        # Add assertions for response data if needed

    def test_get_product_by_id(self):
        # Assuming product_id exists
        response = self.app.get('/api/products/1')
        self.assertEqual(response.status_code, 200)
        # Add assertions for response data if needed

        # Assuming product_id does not exist
        response = self.app.get('/api/products/999')
        self.assertEqual(response.status_code, 404)
        # Add assertions for response data if needed

    @patch('app.create_product')
    def test_create_product(self, mock_create_product):
        mock_create_product.return_value = {'id': 1}
        response = self.app.post('/api/products', json={'name': 'Test Product', 'price': 10.99})
        self.assertEqual(response.status_code, 201)
        # Add assertions for response data if needed

    @patch('app.update_product')
    @patch('app.get_product_by_id')
    def test_update_product(self, mock_get_product_by_id, mock_update_product):
        mock_get_product_by_id.return_value = {'id': 1}
        response = self.app.patch('/api/products/1', json={'name': 'Updated Product'})
        self.assertEqual(response.status_code, 200)
        # Add assertions for response data if needed

        # Assuming product_id does not exist
        mock_get_product_by_id.return_value = None
        response = self.app.patch('/api/products/999', json={'name': 'Updated Product'})
        self.assertEqual(response.status_code, 404)
        # Add assertions for response data if needed

    @patch('app.delete_product')
    @patch('app.get_product_by_id')
    def test_delete_product(self, mock_get_product_by_id, mock_delete_product):
        mock_get_product_by_id.return_value = {'id': 1}
        response = self.app.delete('/api/products/1')
        self.assertEqual(response.status_code, 200)
        # Add assertions for response data if needed

        # Assuming product_id does not exist
        mock_get_product_by_id.return_value = None
        response = self.app.delete('/api/products/999')
        self.assertEqual(response.status_code, 404)
        # Add assertions for response data if needed


if __name__ == '__main__':
    unittest.main()
