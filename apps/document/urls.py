from django.urls import path
from .views import Create_document

urlpatterns = [
    path('<int:employee_id>/', Create_document.as_view(), name='create_document'),
]
