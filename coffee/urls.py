from . import views 
from django.urls import path


urlpatterns = [
    path('', views.CoffeeIndex.as_view(), name='home'),
    path('add-coffee', views.CreateCoffee.as_view(), name='create_coffee'),
    path('edit-coffee/<slug:slug>/', views.EditCoffee.as_view(), name='edit_coffee'),
    path('delete-coffee/<slug:slug>/', views.DeleteCoffee.as_view(), name='delete_coffee'),
]