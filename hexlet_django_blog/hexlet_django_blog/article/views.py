from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from .models import Article, Comment


class IndexView(View):
    template_name = 'articles/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = kwargs.get('tags')
        article_id = kwargs.get('article_id')
        context['message'] = f"Статья номер {article_id}. Тег {tags}"
        context['app_name'] = 'hexlet_django_blog.article'
        context['articles'] = Article.objects.all()
        return context


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )


class ArticleCommentsView(View):
    def get(self, request, article_id, id):
        comment = get_object_or_404(Comment, id=id, article__id=article_id)
        return render(
            request,
            "articles/comment_detail.html",
            context={
                "comment": comment,
                "article_id": article_id,
            }
        )


def home_redirect(request):
    url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
    return redirect(url)
# Create your views here.
