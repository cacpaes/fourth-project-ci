from django.test import TestCase
from coffee.forms import CoffeePostForm, CommentForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.staticfiles import finders

result = finders.find('image/base.css')
searched_locations = finders.searched_locations

"""
class to test form CoffeePostForm
"""
class CoffeePostFormTestCase(TestCase):

    def test_coffee_post_form_invalid(self):
        form = CoffeePostForm(data={
            'coffee_name': 'Colombiano',
        })
        self.assertFalse(form.is_valid())

    def test_coffee_post_form_invalid_image(self):
        form = CoffeePostForm(data={
            'coffee_name': 'Colombiano',
            'coffee_origin': 'Brazil',
            'coffee_brand': 'Nespresso',
            'coffee_content': 'Like coffee',
            'coffee_image': 'teste'
        })
        self.assertFalse(form.is_valid())

    def test_coffee_post_form_invalid_upload_video(self):
        image = SimpleUploadedFile("file.mp4", b"file_content", content_type="video/mp4")
        form = CoffeePostForm(data={
            'coffee_name': 'Colombiano',
            'coffee_origin': 'Brazil',
            'coffee_brand': 'Nespresso',
            'coffee_content': 'Like coffee',
            'coffee_image': image
        })
        self.assertFalse(form.is_valid())

    def test_coffee_post_form_valid(self):
        result = finders.find('image/coffeepage.jpg')

        upload_file = open(result, 'rb')
        file_dict = SimpleUploadedFile(upload_file.name, upload_file.read())

        data = {
            'coffee_name': 'Colombiano',
            'coffee_origin': 'Brazil',
            'coffee_brand': 'Nespresso',
            'coffee_content': 'Like coffee'
        }

        form = CoffeePostForm(data, {'coffee_image': file_dict})
        self.assertTrue(form.is_valid(), form.errors)

"""
class to test form CommentForm
"""
class CommentFormTestCase(TestCase):

    def test_comment_form_valid(self):
        form = CommentForm(data={
            'name': 'Colombiano',
            'email': 'colombiano@gmail.com',
            'body': 'This is a valid'
        })
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_skip_name(self):
        form = CommentForm(data={
            'email': 'colombiano@gmail.com',
            'body': 'This is a valid'
        })
        self.assertFalse(form.is_valid(), form.errors)

    def test_comment_form_invalid_skip_email(self):
        form = CommentForm(data={
            'name': 'Colombiano',
            'body': 'This is a valid'
        })
        self.assertFalse(form.is_valid(), form.errors)


    def test_comment_form_invalid_skip_body(self):
        form = CommentForm(data={
            'email': 'colombiano@gmail.com',
            'name': 'Colombiano'
        })
        self.assertFalse(form.is_valid(), form.errors)
