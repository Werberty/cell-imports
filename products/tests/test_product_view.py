
from django.urls import resolve, reverse
from products import views
from pytest import skip

from .test_products_base import ProductsTestBase


class ProductViewsTest(ProductsTestBase):
    def test_products_home_view_function_is_correct(self):
        view = resolve(reverse('products:home'))
        self.assertIs(view.func, views.home)

    def test_products_product_view_function_is_correct(self):
        view = resolve(reverse('products:products'))
        self.assertIs(view.func, views.products)

    def test_products_delete_product_view_function_is_correct(self):
        view = resolve(reverse('products:delete_product',
                       kwargs={'product_id': 1}))
        self.assertIs(view.func, views.delete_product)

    def test_products_delete_product_returns_302_if_product_found(self):
        # Se redireciona se caso não encrontre produto
        self.make_vendedor()
        self.login_vendedor()
        response = self.client.get(
            reverse('products:delete_product', kwargs={'product_id': 100}))
        self.assertEqual(response.status_code, 302)

    def test_products_edit_product_view_function_is_correct(self):
        view = resolve(reverse('products:edit_product',
                       kwargs={'product_id': 1}))
        self.assertIs(view.func, views.edit_product)
