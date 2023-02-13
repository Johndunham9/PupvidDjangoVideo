"""pupvid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from video import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home_page),
    path('upload', views.upload_video, name='upload_video'),
    path('show_video/<str:id_hash>', views.show_video, name='show_video'),
    path("test/", views.test_view, name="test_view"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('crypto/', include('crypto.urls')),
    path("show_random_video/", views.show_random_video, name="show_random_video"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
