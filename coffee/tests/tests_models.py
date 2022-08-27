from django.contrib.auth.models import User
from django.test import TestCase
from ..models import CoffeePost, Comment

"""
class to test model CoffeePost
"""
class CoffeePostTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='test', password='test')
        CoffeePost.objects.create(
            username=user,
            coffee_name="Colombiano",
            coffee_origin="Brazil",
            coffee_brand="Nespresso",
            coffee_content="I like this coffee"
        )

        CoffeePost.objects.create(
            username=user,
            coffee_name="Italiano",
            coffee_origin="Italy",
            coffee_brand="Veneza",
            coffee_content="I like italy coffee"
        )

    def test_return_str(self):
        coffee = CoffeePost.objects.get(coffee_name="Colombiano")
        self.assertEquals(coffee.__str__(), "Colombiano")

    def test_confirm_data_post(self):
        coffee = CoffeePost.objects.get(coffee_name="Colombiano")
        self.assertEquals(coffee.coffee_name, "Colombiano")
        self.assertEquals(coffee.coffee_origin, "Brazil")
        self.assertEquals(coffee.coffee_brand, "Nespresso")
        self.assertEquals(coffee.coffee_content, "I like this coffee")

    def test_ordering_post(self):
        coffeeAll = CoffeePost.objects.all()
        self.assertEquals(coffeeAll[0].coffee_name, "Italiano")
        self.assertEquals(coffeeAll[1].coffee_name, "Colombiano")
        self.assertGreater(coffeeAll[0].created_on, coffeeAll[1].created_on)

"""
class to test model Comment
"""
class CommentTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='test', password='test')
        post = CoffeePost.objects.create(
            username=user,
            coffee_name="Colombiano",
            coffee_origin="Brazil",
            coffee_brand="Nespresso",
            coffee_content="I like this coffee"
        )
        Comment.objects.create(
            post=post,
            name="Carlos",
            email="carlos@test.com",
            body="I like this post"
        )

        Comment.objects.create(
            post=post,
            name="Test",
            email="test@test.com",
            body="I like this post"
        )

    def test_comment_return_str(self):
        comment = Comment.objects.get(name="Carlos")
        self.assertEquals(comment.__str__(), "Comment I like this post by Carlos")

    def test_confirm_data(self):
        comment = Comment.objects.get(name="Carlos")
        self.assertEquals(comment.name, "Carlos")
        self.assertEquals(comment.email, "carlos@test.com")
        self.assertEquals(comment.body, "I like this post")

    def test_comment_orderind(self):
        comments = Comment.objects.all()
        self.assertEquals(comments[0].name, "Test")
        self.assertEquals(comments[1].name, "Carlos")
        self.assertGreater(comments[0].created_on, comments[1].created_on)
