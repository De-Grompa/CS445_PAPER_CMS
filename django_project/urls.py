"""django_project URL Configuration

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
from pipes import Template
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import register_user
from . import views

urlpatterns = [
    #ADMIN
    path('admin/', admin.site.urls),
    path('account/gradeView', TemplateView.as_view(template_name='gradeView.html'), name='gradeView'),
    #FOR NON_ADMIN
    path('account/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #path('account/register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('account/myBinder', TemplateView.as_view(template_name='myBinder.html'), name = 'myBinder'),
    path('account/paperView', TemplateView.as_view(template_name='paperView.html'), name='paperView'),
    path('account/gradeView', TemplateView.as_view(template_name='gradeView.html'), name='gradeView'),
    path('account/register/', register_user, name='register_user'),
    path('account/StudentA/', TemplateView.as_view(template_name='studentA.html'), name='studentA'),
    path('account/StudentB/', TemplateView.as_view(template_name='studentB.html'), name='studentB'),
    path('account/StudentC/', TemplateView.as_view(template_name='studentC.html'), name='studentC'),
    
    
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
