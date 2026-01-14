from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse


class IndexView(View):
    template_name = 'articles/index.html'

    def get(self, request, tags=None, article_id=None):
        message = f"Статья номер {article_id}. Тег {tags}"
        context = {
            'message': message,
            'app_name': 'hexlet_django_blog.article'
        }
        return render(request, self.template_name, context)


def home_redirect(request):
    url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
    return redirect(url)
# Create your views here.
