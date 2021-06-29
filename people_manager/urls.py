from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('company/', include('apps.company.urls')),
    path('departament/', include('apps.departament.urls')),
    path('document/', include('apps.document.urls')),
    path('employee/', include('apps.employee.urls')),
    path('overtime/', include('apps.overtime.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
