"""
URL configuration for config project - nuam Exchange Group.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Redirección automática de la raíz hacia el frontend oficial en Vercel
    path('', RedirectView.as_view(url='https://proyecto-integrado-caso-nuam.vercel.app', permanent=False), name='root-redirect'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.core.urls')),
]
