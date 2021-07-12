from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from apps.core import views

from apps.employee.api.views import EmployeeViewSet
from apps.overtime.api.views import OvertimeViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/employee', EmployeeViewSet)
router.register(r'api/overtime', OvertimeViewSet)


urlpatterns = [
    path('', include('apps.core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('company/', include('apps.company.urls')),
    path('departament/', include('apps.departament.urls')),
    path('document/', include('apps.document.urls')),
    path('employee/', include('apps.employee.urls')),
    path('overtime/', include('apps.overtime.urls')),
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
