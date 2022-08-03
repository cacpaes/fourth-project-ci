from django.contrib import admin
from .models import CoffeePost
from django_summernote.admin import SummernoteModelAdmin


@admin.register(CoffeePost)
class CoffeePostAdmin(SummernoteModelAdmin):

    list_display = ('coffee_name', 'coffee_origin', 'coffee_brand', 'created_on')
    search_fields = ['coffee_name', 'coffee_origin', 'coffee_brand']
    prepopulated_fields = {'slug': ('coffee_name', 'coffee_brand')}
    list_filter = ('status', 'created_on')
    summernote_fields = ('coffee_content')