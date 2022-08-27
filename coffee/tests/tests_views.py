from django.test import TestCase
from django.urls import reverse

from ..models import CoffeePost, Comment
from django.contrib.auth.models import User


class CoffeeViewsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test', password='test')
        self.user.save()
        self.coffee1 = CoffeePost.objects.create(
            username=self.user,
            coffee_name="Colombiano",
            coffee_origin="Brazil",
            coffee_brand="Nespresso",
            coffee_content="I like this coffee"
        )

        self.coffee1.save()

        self.coffee2 = CoffeePost.objects.create(
            username=self.user,
            coffee_name="Italiano",
            coffee_origin="Italy",
            coffee_brand="Veneza",
            coffee_content="I like italy coffee"
        )

        self.coffee2.save()

        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

    def test_coffee_index_status_code_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200, response)

    def test_coffee_index_template(self):
        response = self.client.get(reverse('home'))
        self.assertTrue('is_paginated' in response.context)

    def test_coffee_index_pagiante(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'index.html')

    def test_coffee_myarea_status_code_200(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('myarea'))
        self.assertEqual(response.status_code, 200, response)

    def test_coffee_myarea_template(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('myarea'))
        self.assertTemplateUsed(response, 'my-area.html')

    def test_detail_coffee_sucess(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('detail', kwargs={'slug': self.coffee2.slug}))
        self.assertEqual(response.status_code, 200, response)
        self.assertTemplateUsed(response, 'detail_coffee.html')

    def test_detail_coffee_not_found_404(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('detail', kwargs={'slug': "teste"}))
        self.assertEqual(response.status_code, 404, response)

    def test_edit_coffee_not_found(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('edit_coffee', kwargs={'slug': "teste"}))
        self.assertEqual(response.status_code, 404, response)

    def test_edit_coffee_user_not_create_403(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('edit_coffee', kwargs={'slug': self.coffee2.slug}))
        self.assertEqual(response.status_code, 403, response)

    def test_edit_coffee_sucess(self):
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('edit_coffee', kwargs={'slug': self.coffee2.slug}))
        self.assertEqual(response.status_code, 302, response)

    def test_delete_coffee_not_found(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('delete_coffee', kwargs={'slug': "teste"}))
        self.assertEqual(response.status_code, 404, response)

    def test_delete_coffee_user_not_create_403(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('delete_coffee', kwargs={'slug': self.coffee2.slug}))
        self.assertEqual(response.status_code, 403, response)

    def test_delete_coffee_sucess(self):
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('delete_coffee', kwargs={'slug': self.coffee2.slug}))
        self.assertEqual(response.status_code, 302, response)

    def test_create_coffee_sucess(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('create_coffee'))
        self.assertTemplateUsed(response, 'add_coffee.html')
        self.assertEqual(response.status_code, 200, response)
        self.assertTrue('form' in response.context)

