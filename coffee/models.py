from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class CoffeePost(models.Model):
    coffee_id = models.SmallAutoField(primary_key=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='post_coffee')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)    
    coffee_name = models.CharField(max_length=30)
    coffee_origin = models.CharField(max_length=30)
    coffee_brand = models.CharField(max_length=30)
    coffee_content = models.TextField(max_length=300, null=True)
    coffee_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(unique=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.coffee_name

    
    def save(self, *args, **kwargs):
        """
        Function to auto generate slugfield
        """
        autoslug = self.coffee_brand + self.coffee_name
        self.slug = slugify(autoslug)
        super(CoffeePost, self).save(*args, **kwargs)