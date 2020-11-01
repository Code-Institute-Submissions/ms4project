from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_records, name='records'),
]
