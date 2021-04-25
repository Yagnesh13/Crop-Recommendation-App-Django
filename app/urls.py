"""croppredi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from croppredi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path("crops/rice/",views.rice,name="rice"),
    path('crops/cotton/',views.cotton,name='cotton'),
    path('crops/maize/',views.maize,name='maize'),
    path('crops/mungbean/',views.mungbean,name='mungbean'),
    path('crops/lentil/',views.lentil,name='lentil'),
    path('crops/jute/',views.jute,name='jute'),
    path('weather/',views.weather,name='weather'),
    path('crops/',views.crops,name='crops'),
    path('crops/cropro/<str:x>',views.croppro,name='cropro')
]
