from django.urls import path
from .views import create_company, edit_company

urlpatterns = [
    path('new', create_company.as_view(), name='create_company'),
    path('edit/<int:pk>/', edit_company.as_view(), name='edit_company'),
]
