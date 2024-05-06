from django.views.generic.detail import DetailView
from .models import Articles

class ArticlesView(DetailView):
    model = Articles
    template_name = 'news/post.html'
