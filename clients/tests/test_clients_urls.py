from django.test import TestCase
from django.urls import reverse


class ClientsUrlsTests(TestCase):
    def test_clients_url_is_correct(self):
        url = reverse('clients:clients')
        self.assertEqual(url, '/clients/')

    def test_create_client_url_is_correct(self):
        url = reverse('clients:create_client')
        self.assertEqual(url, '/clients/create/')

    def test_delete_client_url_is_correct(self):
        url = reverse('clients:delete_client', kwargs={'id_client': 1})
        self.assertEqual(url, '/clients/delete/1')

    def test_edit_client_url_is_correct(self):
        url = reverse('clients:edit_client', kwargs={'id_client': 1})
        self.assertEqual(url, '/clients/edit/1')

    def test_detail_client_url_is_correct(self):
        url = reverse('clients:detail_client', kwargs={'id_client': 1})
        self.assertEqual(url, '/clients/detail/1')
