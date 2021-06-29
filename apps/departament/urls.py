from django.urls import path
from .views import List_departament, Create_departament, Update_departament, Delete_departament

urlpatterns = [
    path('', List_departament.as_view(), name='list_departament'),
    path('new', Create_departament.as_view(), name='create_departament'),
    path('update/<int:pk>/', Update_departament.as_view(), name='update_departament'),
    path('delete/<int:pk>/', Delete_departament.as_view(), name='delete_departament'),
]
