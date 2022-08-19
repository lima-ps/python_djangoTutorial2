"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', RedirectView.as_view(url='/meetups')), #redireciona o caminho absoluto para a view que queremos
    path('meetups/', include('meetups.urls')), #com include eu chamo todas as minhas urls do meu app para cá, onde será o chamado primário da aplicação
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Torna as medias incoroporadas no nosso projeto localizadas e trabalhaveis
