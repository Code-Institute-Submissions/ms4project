from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('cart/<beer_id>', views.add_to_cart, name='add_to_cart'),
    path('adjust/<beer_id>/', views.adjust_cart, name='adjust_cart'),
    path('remove/<beer_id>/', views.remove_from_cart,
         name='remove_from_cart'),
]
