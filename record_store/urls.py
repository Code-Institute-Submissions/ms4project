from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_records, name='records'),
    path('add/', views.add_record, name='add_record'),
    path('edit/<record_id>/', views.edit_record, name='edit_record'),
    path('delete/<record_id>/', views.delete_record, name='delete_record'),
]
