from django.test import TestCase
from products.models import User


class ProductsTestBase(TestCase):
    def setUp(self) -> None:
        self.make_vendedor()
        self.login_vendedor()
        return super().setUp()

    def make_vendedor(self,
                      username='username',
                      password='123456',
                      email='username@rmail.com',
                      ):
        return User.objects.create_user(
            username=username,
            password=password,
            email=email,
        )

    def login_vendedor(self,
                       username='username',
                       password='123456'
                       ):
        self.client.login(username=username, password=password)
