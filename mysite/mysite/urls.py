from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #страничка для админа
    path('', include('mainApp.urls')), #главная страничка
    path('news/', include('news.urls', namespace='news')), #страничка новостей
]
