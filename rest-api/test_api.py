import unittest
import os
import json
from app import app
from db import db

class ProductsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app
        with cls.app.app_context():
            db.init_app(cls.app)
            db.create_all()
        cls.client = cls.app.test_client
        cls.product = {
          'name': 'Test Mesa de jantar Marabraz',
          'description': 'Mesa de jantar em madeira escura com 4 lugares.',
          'price': 200,
          'parent_id': None
        }
        cls.image = {
        	"type": "JPG",
        	"url": "http://i2.marabraz.com.br/800x800/59/00015991138__1_B_ND.jpg",
        	"product_id": 1
        }

    @classmethod
    def tearDownClass(cls):
        os.unlink(os.getenv('DATABASE_URL').split('/')[-1])

    def test_t01_post_new_product(self):
        response = self.client().post('/v1/product', data=self.product)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Mesa', str(response.data))

    def test_t02_get_a_product(self):
        response = self.client().get('/v1/product/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Mesa', str(response.data))

    def test_t03_update_existing_product(self):
        updated = self.product
        updated['price'] = 250
        response = self.client().put('/v1/product/1', data=updated)
        self.assertEqual(response.status_code, 200)
        self.assertIn('250', str(response.data))

    def test_t04_put_new_product(self):
        response = self.client().put('/v1/product/2', data=self.product)
        self.assertEqual(response.status_code, 201)

    def test_t05_delete_product(self):
        response = self.client().delete('/v1/product/2')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Product deleted', str(response.data))

    def test_t06_delete_inexistent_product(self):
        response = self.client().delete('/v1/product/2')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Product not found', str(response.data))

    def test_t01_post_an_image(self):
        response = self.client().post('/v1/image', data=self.image)
        self.assertEqual(response.status_code, 201)
        self.assertIn('JPG', str(response.data))

    def test_t02_get_an_image(self):
        response = self.client().get('/v1/image/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('JPG', str(response.data))

    def test_t03_update_existing_image(self):
        updated = self.image
        updated['type'] = 'GIF'
        updated['url'] = 'http://mydomain.com/myimage.gif'
        response = self.client().put('/v1/image/1', data=updated)
        self.assertEqual(response.status_code, 200)
        self.assertIn('myimage.gif', str(response.data))
        self.assertIn('GIF', str(response.data))

    def test_t04_put_new_image(self):
        response = self.client().put('/v1/image/2', data=self.image)
        self.assertEqual(response.status_code, 201)

    def test_t05_delete_image(self):
        response = self.client().delete('/v1/image/2')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Image deleted', str(response.data))

    def test_t06_delete_inexistent_image(self):
        response = self.client().delete('/v1/image/2')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Image not found', str(response.data))

    def test_t10_add_child_product(self):
        child = self.product
        child['name'] = 'Child'
        child['parent_id'] = 1
        response = self.client().post('/v1/product', data=child)
        self.assertEqual(response.status_code, 201)

    def test_t11_get_children(self):
        response = self.client().get('/v1/product/1/children')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Child', str(response.data))

    def test_t12_product_with_no_children(self):
        response = self.client().get('/v1/product/2/children')
        self.assertEqual(response.status_code, 404)
        self.assertIn('No children found', str(response.data))

    def test_t13_get_childre_from_inexistent_product(self):
        response = self.client().get('/v1/product/100/children')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Product not found', str(response.data))

    def test_t10_get_images_from_product(self):
        response = self.client().get('/v1/product/1/images')
        self.assertEqual(response.status_code, 200)
        self.assertIn('myimage.gif', str(response.data))

    def test_t11_get_images_from_inexistent_product(self):
        response = self.client().get('/v1/product/100/images')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Product not found', str(response.data))

    def test_t12_get_images_from_product_with_no_image(self):
        response = self.client().get('/v1/product/2/images')
        self.assertEqual(response.status_code, 404)
        self.assertIn('No images found', str(response.data))
        


if __name__ == '__main__':
    unittest.main()
