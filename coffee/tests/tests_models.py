from django.test import TestCase
from ..models import CoffeePost
from django.test.runner import DiscoverRunner

class CoffeePostTestCase(TestCase):

    def setUp(self):

        CoffeePost.objects.create(
            coffee_name="Colombiano",
            coffee_origin="Brazil",
            coffee_brand="Nespresso",
            coffee_content="I like this coffee"
        )

    def test_return_str(self):
        coffee =  Pessoa.objects.get(coffee_name="Colombiano")
        self.assertEquals(coffee.__str__, "Colombia")
