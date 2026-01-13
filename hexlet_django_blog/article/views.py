from django.shortcuts import render
from django.views import View


class IndexView(View):
    template_name = 'articles/index.html'

    def get(self, request):
        context = {
            'app_name': 'hexlet_django_blog.article'
        }
        return render(request, self.template_name, context)
# Create your views here.
