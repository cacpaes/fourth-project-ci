from . import views 
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.CoffeeIndex.as_view(), name='home'),
    path('my-area', views.CoffeeMyarea.as_view(), name='myarea'),
    path('detail/<slug:slug>/', views.detail_coffee, name='detail'),
    path('add-coffee', views.CreateCoffee.as_view(), name='create_coffee'),
    path('edit-coffee/<slug:slug>/', views.EditCoffee.as_view(), name='edit_coffee'),
    path('delete-coffee/<slug:slug>/', views.DeleteCoffee.as_view(), name='delete_coffee'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)