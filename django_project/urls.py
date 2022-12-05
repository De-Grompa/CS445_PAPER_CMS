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
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    #ADMIN
    path('admin/', admin.site.urls),
    path('account/gradeView', TemplateView.as_view(template_name='gradeView.html'), name='gradeView'),
    #FOR NON_ADMIN
    path('account/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('account/register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('account/myBinder', TemplateView.as_view(template_name='myBinder.html'), name = 'myBinder'),
    path('account/paperView', TemplateView.as_view(template_name='paperView.html'), name='paperView'),
    path('account/gradeView', TemplateView.as_view(template_name='gradeView.html'), name='gradeView'),
    ]
