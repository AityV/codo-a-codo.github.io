"""
URL configuration for webantartico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from core import views as core_views
from ddbbdatos import views as ddbbdatos_views
from ddbbdatos.views import process_form
from destinations import views as destinations_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name='index'),
    path('destinations', destinations_views.destinations, name='destinations'),
    path('packages', core_views.packages, name='packages'),
    path('contact/', ddbbdatos_views.contact, name='contact'),
    path('construction', core_views.construction, name='construction'),
    path('process_form/', process_form, name='process_form')
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
