from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from .models import Article


class IndexView(View):
    template_name = 'articles/index.html'

    def get_context_data(self, request, **kwargs):
        tags = kwargs.get('tags')
        article_id = kwargs.get('article_id')
        message = f"Статья номер {article_id}. Тег {tags}"
        articles = Article.objects.all()
        context = {
            'message': message,
            'app_name': 'hexlet_django_blog.article',
            'articles': articles
        }
        return render(request, self.template_name, context)


def home_redirect(request):
    url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
    return redirect(url)
# Create your views here.
