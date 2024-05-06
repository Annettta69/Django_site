from django.urls import path, include
from django.views.generic import ListView, DetailView
from .models import Articles
from .views import ArticlesView

app_name = 'news'

urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],template_name="news/posts.html")),
    path('<int:pk>/', ArticlesView.as_view(), name="news/post.html")
]

"""
app_name = 'news'

urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], template_name="news/posts.html")),
    path('<int:pk>/', ArticlesView.as_view(), name="Articles")
]
"""