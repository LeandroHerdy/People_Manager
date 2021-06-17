from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('apps.core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('company/', include('apps.company.urls')),
    path('employee/', include('apps.employee.urls')),
    path('admin/', admin.site.urls),
]
