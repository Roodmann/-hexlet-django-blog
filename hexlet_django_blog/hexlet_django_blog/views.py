from django.shortcuts import render
from django.views.generic import TemplateView
from hexlet_django_blog.article.models import Article

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "World"
        context["articles"] = Article.objects.all()
        return context


def about(request):
    return render(request, "about.html")