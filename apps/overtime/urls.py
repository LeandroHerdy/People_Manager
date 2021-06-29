from django.urls import path
from .views import List_overtime, Update_overtime, Delete_overtime, Create_Overtime

urlpatterns = [
    path('', List_overtime.as_view(), name='list_overtime'),
    path('update<int:pk>/', Update_overtime.as_view(), name='update_overtime'),
    path('delete<int:pk>/', Delete_overtime.as_view(), name='delete_overtime'),
    path('new/', Create_Overtime.as_view(), name='create_overtime'),
]
