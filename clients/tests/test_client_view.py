from clients import views
from django.urls import resolve, reverse

from .test_client_base import ClientsTestBase


class ClientsViewsTests(ClientsTestBase):
    def test_clients_views_function_is_correct(self):
        view = resolve(reverse('clients:clients'))
        self.assertIs(view.func, views.clients)

    def test_create_client_views_function_is_correct(self):
        view = resolve(reverse('clients:create_client'))
        self.assertIs(view.func, views.create_client)

    def test_delete_client_views_function_is_correct(self):
        view = resolve(
            reverse('clients:delete_client', kwargs={'id_client': 1}))
        self.assertIs(view.func, views.delete_client)

    def test_delete_client_return_302_if_not_found_client(self):
        self.make_vendedor()
        self.login_vendedor()

        response = self.client.get(reverse('clients:delete_client',
                                           kwargs={'id_client': 1000}))

        self.assertEqual(response.status_code, 302)

    def test_detail_client_views_function_is_correct(self):
        view = resolve(
            reverse('clients:detail_client', kwargs={'id_client': 1}))
        self.assertIs(view.func, views.detail_client)

    def test_edit_client_views_function_is_correct(self):
        view = resolve(
            reverse('clients:edit_client', kwargs={'id_client': 1}))
        self.assertIs(view.func, views.edit_client)
