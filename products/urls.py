from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_beers, name='beers'),
    path('int:<beer_id>/', views.beer_detail, name='beer_detail'),
    path('add/', views.add_beer, name='add_beer'),
]
