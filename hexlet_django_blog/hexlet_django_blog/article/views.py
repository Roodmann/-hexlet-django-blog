from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from .forms import CommentArticleForm, ArticleForm
from .models import Article, Comment, ArticleComment


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


class CommentArticleView(View):
    # если метод POST, то мы обрабатываем данные
    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST)  # Получаем данные формы из запроса
        if form.is_valid():  # Проверяем данные формы на корректность
            comment = ArticleComment(
                content=form.cleaned_data[
                    "content"
                ],  # Получаем очищенные данные из поля content
            )  #  и создаем новый комментарий
            comment.save()

    # если метод GET, то создаем пустую форму
    def get(self, request, *args, **kwargs):
        form = CommentArticleForm()  # Создаем экземпляр нашей формы
        return render(
            request, "comment.html", {"form": form}
        )  # Передаем нашу форму в контексте


class ArticleCommentFormView(View):
    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            # Создаем комментарий
            comment = ArticleComment(
                article=get_object_or_404(Article, pk=kwargs['article_id']),
                user=request.user  # если есть авторизация
            )
            comment.save()
            return redirect('article_detail', pk=kwargs['article_id'])
        # В случае ошибки можно вернуть обратно или показать сообщение
        return redirect('article_detail', pk=kwargs['article_id'])


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/form_create.html", {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid(): # Если данные корректные, то сохраняем данные формы
            form.save()
            messages.success(request, "Статья успешно создана!")
            return redirect('articles') # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        else:
            # Можно добавить сообщение об ошибке
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
        return render(request, 'articles/form_create.html', {'form': form})


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        messages.info(request, "Редактирование статьи")
        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id, "is_get": True}
        )
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Статья успешно обновлена.")
            return redirect("article_detail", article_id)

        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id,}
        )


def home_redirect(request):
    url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
    return redirect(url)
# Create your views here.



