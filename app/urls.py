from django.contrib import admin
from django.urls import path
from croppredi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('weather/',views.weather,name='weather'),
    path('crops/',views.crops,name='crops'),
    path('crops/cropro/<str:x>',views.croppro,name='cropro')
]
