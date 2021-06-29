from django.urls import path
from .views import List_employee, Update_employee, Delete_employee, Create_employee

urlpatterns = [
    path('', List_employee.as_view(), name='list_employee'),
    path('new/', Create_employee.as_view(), name='create_employee'),
    path('Update/<int:pk>/', Update_employee.as_view(), name='update_employee'),
    path('delete/<int:pk>/', Delete_employee.as_view(), name='delete_employee'),
]
