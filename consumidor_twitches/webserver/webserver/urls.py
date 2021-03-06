"""webserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from webserver import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pod_name/', views.get_hostname, name='get_hostname'),
    path('home/', views.home_json, name='home_json'),
    path('info_twitches/', views.get_twitches, name='info_twitches'),
    
    
    path('', views.home, name='home_page'),
    
    
    
]
