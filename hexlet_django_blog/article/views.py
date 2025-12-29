from django.shortcuts import render


def index(request):
    context = {
        'app_name': 'hexlet_django_blog.article'
    }
    return render(request, 'articles/index.html', context)
# Create your views here.
