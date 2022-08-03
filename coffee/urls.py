from . import views 
from django.urls import path


urlpatterns = [
    path('', views.CoffeeIndex.as_view(), name='home'),
]