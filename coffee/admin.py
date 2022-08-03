from django.contrib import admin
from .models import Coffee
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Coffee)
class CoffeeAdmin(SummernoteModelAdmin):

    summernote_fields = ('coffee_content')
