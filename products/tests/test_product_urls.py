from django.test import TestCase
from django.urls import reverse


class TestProductUrls(TestCase):
    def test_home_url_is_correct(self):
        url = reverse('products:home')
        self.assertEqual(url, '/')

    def test_product_url_is_correct(self):
        url = reverse('products:products')
        self.assertEqual(url, '/products/')

    def test_delete_product_url_is_correct(self):
        url = reverse('products:delete_product', kwargs={'product_id': 1})
        self.assertEqual(url, '/products/delete/1')

    def test_edit_product_url_is_correct(self):
        url = reverse('products:edit_product', kwargs={'product_id': 1})
        self.assertEqual(url, '/products/edit/1')
